"""Flask Web API for Text-to-Speech Tool"""

from flask import Flask, request, jsonify
from tts_tool import TextToSpeech
from tts_tool.config import Config
import traceback

# Create Flask app instance (required by Vercel)
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Health check endpoint"""
    return jsonify({
        "status": "ok",
        "message": "Text-to-Speech API is running"
    })


@app.route('/api/speak', methods=['POST'])
def speak():
    """
    Convert text to speech
    
    Expected JSON payload:
    {
        "text": "Hello world",
        "engine": "pyttsx3",  # optional, default: pyttsx3
        "language": "en",      # optional, default: en
        "rate": 1.0,           # optional, default: 1.0
        "volume": 1.0          # optional, default: 1.0
    }
    """
    try:
        data = request.get_json() or {}
        text = data.get('text')
        
        if not text:
            return jsonify({"error": "Missing required field: text"}), 400
        
        engine = data.get('engine', 'pyttsx3')
        language = data.get('language', 'en')
        rate = float(data.get('rate', 1.0))
        volume = float(data.get('volume', 1.0))
        
        # Validate engine choice
        if engine not in ['pyttsx3', 'gtts', 'mock']:
            return jsonify({"error": f"Invalid engine: {engine}"}), 400
        
        # Initialize TTS
        tts = TextToSpeech(
            engine=engine,
            language=language,
            rate=rate,
            volume=volume
        )
        
        # Get info about the engine
        info = tts.get_info()
        
        # Speak the text
        tts.speak(text)
        
        return jsonify({
            "status": "success",
            "message": "Text spoken successfully",
            "engine_info": info
        })
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "traceback": traceback.format_exc()
        }), 500


@app.route('/api/info', methods=['GET'])
def get_info():
    """Get TTS tool information"""
    try:
        config = Config()
        return jsonify({
            "default_engine": config.get('default_engine'),
            "default_language": config.get('default_language'),
            "default_rate": config.get('default_rate'),
            "default_volume": config.get('default_volume'),
            "supported_languages": config.get('supported_languages', []),
            "available_engines": ["pyttsx3", "gtts", "mock"]
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    # For local development
    app.run(debug=True, host='0.0.0.0', port=5000)
