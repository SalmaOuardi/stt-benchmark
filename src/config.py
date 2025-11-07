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
DATA_ROOT = Path(os.getenv("AUDIO_DATA_DIR", "data/processed")).expanduser()

# Validate required configuration
if not AZURE_API_KEY:
    raise EnvironmentError(
        "AZURE_API_KEY is not set. Please add it to your environment or .env file."
    )

# Azure speech models and their target endpoints
MODELS = {
    "whisper": {
        "url": f"{AZURE_ENDPOINT}/openai/deployments/whisper/audio/translations?api-version=2024-06-01",
        "type": "whisper",
        "deployment": "whisper",
        "api_version": "2024-06-01",
    },
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

# Enable LLM-based normalization for more accurate WER calculation
USE_LLM_NORMALIZATION = os.getenv("USE_LLM_NORMALIZATION", "true").lower() == "true"
