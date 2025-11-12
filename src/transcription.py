"""
Transcription API module.
Handles communication with Azure OpenAI speech models.
"""

import base64
import os
import time
from pathlib import Path
from typing import Dict, Any

import requests
from openai import AzureOpenAI

from config import (
    AZURE_API_KEY,
    AZURE_ENDPOINT,
    MODELS,
    TRANSCRIPTION_PROMPT
)


def test_transcription(audio_path: Path, model_name: str) -> Dict[str, Any]:
    """
    Test transcription models using audio transcriptions API.

    Args:
        audio_path: Path to audio file
        model_name: Name of the model to test

    Returns:
        Dictionary containing test results with keys:
        - model: Model name
        - transcript: Transcribed text (if successful)
        - latency: Request latency in seconds
        - success: Boolean indicating success
        - error: Error message (if failed)
    """
    print(f"🎤 Testing {model_name}...")

    with open(audio_path, "rb") as f:
        files = {"file": f}
        headers = {"api-key": AZURE_API_KEY}

        start = time.time()
        response = requests.post(MODELS[model_name]["url"], headers=headers, files=files)
        latency = time.time() - start

    if response.ok:
        return {
            "model": model_name,
            "transcript": response.json().get("text", ""),
            "latency": latency,
            "success": True
        }
    else:
        return {
            "model": model_name,
            "error": response.text,
            "success": False
        }


def test_gpt_audio(audio_path: Path, model_name: str) -> Dict[str, Any]:
    """
    Test GPT audio models using chat completions API.

    Args:
        audio_path: Path to audio file
        model_name: Name of the model to test

    Returns:
        Dictionary containing test results with keys:
        - model: Model name
        - transcript: Transcribed text (if successful)
        - latency: Request latency in seconds
        - success: Boolean indicating success
        - error: Error message (if failed)
    """
    print(f"🎤 Testing {model_name}...")

    client = AzureOpenAI(
        api_key=AZURE_API_KEY,
        api_version=MODELS[model_name]["api_version"],
        azure_endpoint=AZURE_ENDPOINT
    )

    # Encode audio to base64
    with open(audio_path, "rb") as f:
        audio_b64 = base64.b64encode(f.read()).decode()

    # Determine audio format
    audio_suffix = audio_path.suffix.lower() if isinstance(audio_path, Path) else os.path.splitext(audio_path)[1].lower()
    audio_format = "wav" if audio_suffix == ".wav" else "mp3"

    try:
        start = time.time()
        response = client.chat.completions.create(
            model=MODELS[model_name]["deployment"],
            modalities=["text"],
            audio={"voice": "alloy", "format": audio_format},
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "input_audio",
                        "input_audio": {"data": audio_b64, "format": audio_format}
                    },
                    {
                        "type": "text",
                        "text": TRANSCRIPTION_PROMPT
                    }
                ]
            }]
        )
        latency = time.time() - start

        return {
            "model": model_name,
            "transcript": response.choices[0].message.content,
            "latency": latency,
            "success": True
        }
    except Exception as e:
        return {
            "model": model_name,
            "error": str(e),
            "success": False
        }
