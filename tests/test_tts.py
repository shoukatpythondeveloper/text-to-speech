"""Unit tests for TextToSpeech tool"""

import pytest
import os
from tts_tool import TextToSpeech
from tts_tool.engines import MockEngine, Pyttsx3Engine


class TestTextToSpeech:
    """Test TextToSpeech main class"""
    
    def test_initialization(self):
        """Test TTS initialization"""
        tts = TextToSpeech(engine='mock', language='en')
        assert tts.language == 'en'
        assert tts.engine_name == 'mock'
    
    def test_invalid_engine(self):
        """Test invalid engine raises error"""
        with pytest.raises(ValueError):
            TextToSpeech(engine='invalid')
    
    def test_set_rate(self):
        """Test setting speech rate"""
        tts = TextToSpeech(engine='mock')
        tts.set_rate(1.5)
        assert tts.rate == 1.5
        
        # Test bounds
        tts.set_rate(0.2)
        assert tts.rate == 0.5  # Minimum
        
        tts.set_rate(3.0)
        assert tts.rate == 2.0  # Maximum
    
    def test_set_volume(self):
        """Test setting volume"""
        tts = TextToSpeech(engine='mock')
        tts.set_volume(0.8)
        assert tts.volume == 0.8
        
        # Test bounds
        tts.set_volume(-0.5)
        assert tts.volume == 0.0  # Minimum
        
        tts.set_volume(1.5)
        assert tts.volume == 1.0  # Maximum
    
    def test_get_info(self):
        """Test getting configuration info"""
        tts = TextToSpeech(engine='mock', language='es', rate=0.9, volume=0.7)
        info = tts.get_info()
        
        assert info['engine'] == 'mock'
        assert info['language'] == 'es'
        assert info['rate'] == 0.9
        assert info['volume'] == 0.7
    
    def test_speak_empty_text(self):
        """Test speaking empty text"""
        tts = TextToSpeech(engine='mock')
        tts.speak("")  # Should not raise error
    
    def test_speak_with_mock(self):
        """Test speaking with mock engine"""
        tts = TextToSpeech(engine='mock')
        tts.speak("Test message")
        assert tts.engine.last_spoken == "Test message"


class TestMockEngine:
    """Test MockEngine"""
    
    def test_mock_speak(self):
        """Test mock engine speak"""
        engine = MockEngine()
        engine.speak("Hello")
        assert engine.last_spoken == "Hello"
    
    def test_mock_rate(self):
        """Test mock engine rate"""
        engine = MockEngine()
        engine.set_rate(1.5)
        assert engine.rate == 1.5
    
    def test_mock_volume(self):
        """Test mock engine volume"""
        engine = MockEngine()
        engine.set_volume(0.5)
        assert engine.volume == 0.5


class TestPyttsx3Engine:
    """Test Pyttsx3Engine"""
    
    def test_initialization(self):
        """Test pyttsx3 initialization"""
        engine = Pyttsx3Engine()
        assert engine.language == 'en'
        assert engine.volume == 1.0
    
    def test_set_rate(self):
        """Test pyttsx3 rate setting"""
        engine = Pyttsx3Engine()
        engine.set_rate(0.8)
        assert engine.rate == 160
    
    def test_set_volume(self):
        """Test pyttsx3 volume setting"""
        engine = Pyttsx3Engine()
        engine.set_volume(0.5)
        assert engine.volume == 0.5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
