"""Basic usage examples for Text-to-Speech tool"""

from tts_tool import TextToSpeech


def example_basic_speak():
    """Example: Basic text-to-speech"""
    print("Example 1: Basic speak")
    tts = TextToSpeech()
    tts.speak("Hello, this is a text-to-speech example!")


def example_save_to_file():
    """Example: Save speech to file"""
    print("\nExample 2: Save to file")
    tts = TextToSpeech()
    tts.save_to_file("Saving this message to a file", "output.wav")


def example_adjust_parameters():
    """Example: Adjust speech parameters"""
    print("\nExample 3: Adjust parameters")
    tts = TextToSpeech()
    
    # Slow speech
    tts.set_rate(0.8)
    tts.speak("This is slow speech")
    
    # Fast speech
    tts.set_rate(1.5)
    tts.speak("This is fast speech")
    
    # Quiet speech
    tts.set_volume(0.5)
    tts.speak("This is quiet speech")


def example_different_language():
    """Example: Different language"""
    print("\nExample 4: Different language")
    tts = TextToSpeech(language='es')  # Spanish
    tts.speak("Hola, esto es un ejemplo en español")


def example_google_tts():
    """Example: Using Google TTS"""
    print("\nExample 5: Google TTS")
    tts = TextToSpeech(engine='gtts')
    tts.speak("Using Google Text-to-Speech")


def example_get_info():
    """Example: Get configuration info"""
    print("\nExample 6: Get info")
    tts = TextToSpeech(engine='pyttsx3', language='en', rate=1.2, volume=0.8)
    info = tts.get_info()
    
    print("Current configuration:")
    for key, value in info.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    try:
        example_basic_speak()
        example_save_to_file()
        example_adjust_parameters()
        example_different_language()
        example_get_info()
        
        # Uncomment to test Google TTS (requires internet)
        # example_google_tts()
        
    except Exception as e:
        print(f"Error running examples: {e}")
