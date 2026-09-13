"""Text-to-Speech Tool Package"""

from .tts import TextToSpeech
from .engines import TTSEngine, Pyttsx3Engine, GTTSEngine

__version__ = "1.0.0"
__all__ = ["TextToSpeech", "TTSEngine", "Pyttsx3Engine", "GTTSEngine"]
