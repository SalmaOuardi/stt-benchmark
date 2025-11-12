"""
Configuration module for Speech-to-Text benchmark testing.
Handles environment variables, API configuration, and model definitions.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Azure OpenAI configuration
AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT", "https://draftspeechtotext.cognitiveservices.azure.com")

# Data directories - using only data/off/processed
DATA_ROOT_BASE = Path(os.getenv("AUDIO_DATA_DIR", "data")).expanduser()

# Use only data/off/processed directory
DATA_ROOTS = [DATA_ROOT_BASE / "off" / "processed"]

# For backward compatibility, keep DATA_ROOT as the first directory
DATA_ROOT = DATA_ROOTS[0]

# Validate required configuration
if not AZURE_API_KEY:
    raise EnvironmentError(
        "AZURE_API_KEY is not set. Please add it to your environment or .env file."
    )

# Azure speech models and their target endpoints
MODELS = {
    "gpt-audio": {
        "url": f"{AZURE_ENDPOINT}/openai/deployments/gpt-audio/chat/completions?api-version=2025-01-01-preview",
        "deployment": "gpt-audio",
        "type": "chat",
        "api_version": "2025-01-01-preview",
    },
    "gpt-audio-mini": {
        "url": f"{AZURE_ENDPOINT}/openai/deployments/gpt-audio-mini/chat/completions?api-version=2025-01-01-preview",
        "deployment": "gpt-audio-mini",
        "type": "chat",
        "api_version": "2025-01-01-preview",
    },
    "gpt-4o-transcribe": {
        "url": f"{AZURE_ENDPOINT}/openai/deployments/gpt-4o-transcribe/audio/transcriptions?api-version=2025-03-01-preview",
        "deployment": "gpt-4o-transcribe",
        "type": "transcription",
        "api_version": "2025-03-01-preview",
    },
    "gpt-4o-mini-transcribe": {
        "url": f"{AZURE_ENDPOINT}/openai/deployments/gpt-4o-mini-transcribe/audio/transcriptions?api-version=2025-03-01-preview",
        "deployment": "gpt-4o-mini-transcribe",
        "type": "transcription",
        "api_version": "2025-03-01-preview",
    },
    "gpt-4o-audio-preview": {
        "url": f"{AZURE_ENDPOINT}/openai/deployments/gpt-4o-audio-preview/chat/completions?api-version=2025-01-01-preview",
        "deployment": "gpt-4o-audio-preview",
        "type": "chat",
        "api_version": "2025-01-01-preview",
    }
}

# Active models to test
ACTIVE_MODELS = [
    "gpt-audio",
    "gpt-audio-mini",
    "gpt-4o-transcribe",
    "gpt-4o-mini-transcribe",
    "gpt-4o-audio-preview",
]

# Transcription prompt for GPT audio models
TRANSCRIPTION_PROMPT = "Transcribe this French audio exactly. Return only the transcript."

# Rate limiting delay between API calls (seconds)
RATE_LIMIT_DELAY = 1

# Mistral configuration for LLM-based normalization
# Using the correct Azure OpenAI format with deployment name
MISTRAL_DEPLOYMENT = "mistral-small-2503"
MISTRAL_ENDPOINT = f"{AZURE_ENDPOINT}/openai/deployments/{MISTRAL_DEPLOYMENT}/chat/completions?api-version=2024-05-01-preview"

# Disable LLM-based normalization - calculate WER using raw transcripts and references
USE_LLM_NORMALIZATION = False
