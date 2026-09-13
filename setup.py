"""Setup script for Text-to-Speech Tool"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="text-to-speech",
    version="1.0.0",
    author="Shoukat Python Developer",
    author_email="shoukat@example.com",
    description="A Python text-to-speech tool supporting multiple TTS engines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shoukatpythondeveloper/text-to-speech",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pyttsx3>=2.90",
        "gtts>=2.4.0",
        "PyYAML>=6.0",
        "click>=8.1.7",
        "colorama>=0.4.6",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "pytest-cov>=4.1.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "tts=main:cli",
        ],
    },
)
