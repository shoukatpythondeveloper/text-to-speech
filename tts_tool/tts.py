"""Main TextToSpeech Class"""

from typing import Optional
from .engines import TTSEngine, Pyttsx3Engine, GTTSEngine, MockEngine
from .config import Config


class TextToSpeech:
    """Main Text-to-Speech converter class"""
    
    def __init__(self, 
                 engine: str = 'pyttsx3',
                 language: str = 'en',
                 rate: float = 1.0,
                 volume: float = 1.0):
        """
        Initialize TextToSpeech converter
        
        Args:
            engine: TTS engine to use ('pyttsx3', 'gtts', 'mock')
            language: Language code (e.g., 'en', 'es', 'fr')
            rate: Speech rate (0.5 - 2.0)
            volume: Volume level (0.0 - 1.0)
        """
        self.engine_name = engine
        self.language = language
        self.rate = rate
        self.volume = volume
        
        # Initialize engine
        self.engine = self._create_engine(engine, language)
        self.set_rate(rate)
        self.set_volume(volume)
    
    def _create_engine(self, engine_name: str, language: str) -> TTSEngine:
        """Create TTS engine based on name"""
        engines = {
            'pyttsx3': Pyttsx3Engine,
            'gtts': GTTSEngine,
            'mock': MockEngine,
        }
        
        if engine_name not in engines:
            raise ValueError(f"Unknown engine: {engine_name}. Available: {list(engines.keys())}")
        
        return engines[engine_name](language)
    
    def speak(self, text: str) -> None:
        """Speak the text"""
        if not text:
            print("Error: Empty text provided")
            return
        
        try:
            self.engine.speak(text)
        except Exception as e:
            print(f"Error speaking: {e}")
    
    def save_to_file(self, text: str, filename: str) -> None:
        """Save speech to file"""
        if not text:
            print("Error: Empty text provided")
            return
        
        try:
            self.engine.save_to_file(text, filename)
        except Exception as e:
            print(f"Error saving file: {e}")
    
    def set_rate(self, rate: float) -> None:
        """Set speech rate"""
        self.rate = max(0.5, min(2.0, rate))
        self.engine.set_rate(self.rate)
    
    def set_volume(self, volume: float) -> None:
        """Set volume level"""
        self.volume = max(0.0, min(1.0, volume))
        self.engine.set_volume(self.volume)
    
    def set_language(self, language: str) -> None:
        """Change language"""
        self.language = language
        if hasattr(self.engine, 'set_language'):
            self.engine.set_language(language)
    
    def get_info(self) -> dict:
        """Get current TTS configuration"""
        return {
            'engine': self.engine_name,
            'language': self.language,
            'rate': self.rate,
            'volume': self.volume,
        }
