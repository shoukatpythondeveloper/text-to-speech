"""Configuration Module"""

import os
import yaml
from typing import Dict, Any


class Config:
    """Configuration handler for TTS tool"""
    
    DEFAULT_CONFIG = {
        'default_engine': 'pyttsx3',
        'default_language': 'en',
        'default_rate': 1.0,
        'default_volume': 1.0,
        'output_format': 'mp3',
        'supported_languages': ['en', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ja', 'ko', 'zh'],
    }
    
    def __init__(self, config_file: str = 'config.yaml'):
        """Initialize configuration"""
        self.config_file = config_file
        self.config = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file or use defaults"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    return yaml.safe_load(f) or self.DEFAULT_CONFIG
            except Exception as e:
                print(f"Error loading config: {e}. Using defaults.")
                return self.DEFAULT_CONFIG.copy()
        else:
            return self.DEFAULT_CONFIG.copy()
    
    def save_config(self) -> None:
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                yaml.dump(self.config, f, default_flow_style=False)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value"""
        self.config[key] = value
