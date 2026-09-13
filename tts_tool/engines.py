"""Text-to-Speech Engine Implementations"""

from abc import ABC, abstractmethod
from typing import Optional
import pyttsx3
from gtts import gTTS
import os


class TTSEngine(ABC):
    """Abstract base class for TTS engines"""
    
    @abstractmethod
    def speak(self, text: str) -> None:
        """Speak the text"""
        pass
    
    @abstractmethod
    def save_to_file(self, text: str, filename: str) -> None:
        """Save speech to file"""
        pass
    
    @abstractmethod
    def set_rate(self, rate: float) -> None:
        """Set speech rate (speed)"""
        pass
    
    @abstractmethod
    def set_volume(self, volume: float) -> None:
        """Set volume level (0.0 - 1.0)"""
        pass


class Pyttsx3Engine(TTSEngine):
    """pyttsx3 TTS Engine - Offline engine"""
    
    def __init__(self, language: str = 'en'):
        """Initialize pyttsx3 engine"""
        self.engine = pyttsx3.init()
        self.language = language
        self.rate = 200
        self.volume = 1.0
        
        # Set default properties
        self.engine.setProperty('rate', self.rate)
        self.engine.setProperty('volume', self.volume)
    
    def speak(self, text: str) -> None:
        """Speak text using pyttsx3"""
        self.engine.say(text)
        self.engine.runAndWait()
    
    def save_to_file(self, text: str, filename: str) -> None:
        """Save speech to WAV file"""
        try:
            self.engine.save_to_file(text, filename)
            self.engine.runAndWait()
            print(f"Audio saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")
    
    def set_rate(self, rate: float) -> None:
        """Set speech rate (0.5 - 2.0)"""
        self.rate = int(rate * 200)
        self.engine.setProperty('rate', self.rate)
    
    def set_volume(self, volume: float) -> None:
        """Set volume (0.0 - 1.0)"""
        self.volume = max(0.0, min(1.0, volume))
        self.engine.setProperty('volume', self.volume)
    
    def set_voice(self, voice_id: int = 0) -> None:
        """Set voice (0 for male, 1 for female)"""
        voices = self.engine.getProperty('voices')
        if voice_id < len(voices):
            self.engine.setProperty('voice', voices[voice_id].id)


class GTTSEngine(TTSEngine):
    """Google Text-to-Speech Engine - Online engine"""
    
    def __init__(self, language: str = 'en'):
        """Initialize gTTS engine"""
        self.language = language
        self.rate = 1.0
        self.volume = 1.0
    
    def speak(self, text: str) -> None:
        """Speak text using Google TTS"""
        try:
            tts = gTTS(text=text, lang=self.language, slow=False)
            # Save to temporary file and play
            temp_file = "temp_tts.mp3"
            tts.save(temp_file)
            os.system(f"ffplay -nodisp -autoexit {temp_file}" if os.name == 'posix' 
                     else f"start {temp_file}" if os.name == 'nt' 
                     else f"xdg-open {temp_file}")
        except Exception as e:
            print(f"Error speaking: {e}")
    
    def save_to_file(self, text: str, filename: str) -> None:
        """Save speech to MP3 file"""
        try:
            tts = gTTS(text=text, lang=self.language, slow=False)
            tts.save(filename)
            print(f"Audio saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")
    
    def set_rate(self, rate: float) -> None:
        """Set speech rate (gTTS doesn't support rate directly)"""
        # gTTS has limited rate support, only slow parameter
        self.rate = rate
    
    def set_volume(self, volume: float) -> None:
        """Set volume (gTTS doesn't support volume)"""
        self.volume = max(0.0, min(1.0, volume))
    
    def set_language(self, language: str) -> None:
        """Set language"""
        self.language = language


class MockEngine(TTSEngine):
    """Mock engine for testing"""
    
    def __init__(self, language: str = 'en'):
        self.language = language
        self.rate = 1.0
        self.volume = 1.0
        self.last_spoken = None
    
    def speak(self, text: str) -> None:
        self.last_spoken = text
        print(f"[Mock] Speaking: {text}")
    
    def save_to_file(self, text: str, filename: str) -> None:
        print(f"[Mock] Saved to {filename}")
    
    def set_rate(self, rate: float) -> None:
        self.rate = rate
    
    def set_volume(self, volume: float) -> None:
        self.volume = max(0.0, min(1.0, volume))
