# Text-to-Speech Tool

A Python-based text-to-speech tool that converts text into natural-sounding audio using multiple TTS engines.

## Features

- Multiple TTS engine support (pyttsx3, gTTS, Azure)
- Support for multiple languages
- Adjustable speech rate and volume
- Save audio to file (MP3, WAV)
- Command-line interface
- Python API for easy integration

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/shoukatpythondeveloper/text-to-speech.git
cd text-to-speech

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

### Using the Command Line

```bash
# Basic usage
python main.py "Hello, this is a text to speech demo"

# Specify language
python main.py "Bonjour" --language fr

# Save to file
python main.py "Hello world" --output audio.mp3

# Adjust speed and volume
python main.py "Hello" --rate 0.8 --volume 0.9
```

### Using as a Python Module

```python
from tts_tool import TextToSpeech

# Initialize TTS
tts = TextToSpeech(engine='pyttsx3', language='en')

# Speak text
tts.speak("Hello, world!")

# Save to file
tts.save_to_file("Hello, world!", "output.mp3")

# Set speech parameters
tts.set_rate(0.8)  # Slower speech
tts.set_volume(0.9)  # Volume level
```

## Supported Engines

1. **pyttsx3** - Offline, cross-platform, no internet required
2. **gTTS** - Google Text-to-Speech, supports many languages
3. **Azure** - Azure Speech Service (requires API key)

## Configuration

Edit `config.yaml` to customize default settings:

```yaml
default_engine: pyttsx3
default_language: en
default_rate: 1.0
default_volume: 1.0
output_format: mp3
```

## Usage Examples

See `examples/` directory for more detailed examples.

## Testing

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details

## Troubleshooting

### Audio not playing
- Check system audio output is enabled
- Try different engine: `--engine gtts`

### Language not supported
- Check supported languages for your engine
- Use language code (e.g., 'en', 'es', 'fr')

## Support

For issues and questions, please open an issue on GitHub.
