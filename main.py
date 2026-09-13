"""Command-line interface for Text-to-Speech Tool"""

import click
from colorama import Fore, Style
from tts_tool import TextToSpeech
from tts_tool.config import Config


@click.group()
def cli():
    """Text-to-Speech Tool - Convert text to natural speech"""
    pass


@cli.command()
@click.argument('text')
@click.option('--engine', '-e', default='pyttsx3', 
              type=click.Choice(['pyttsx3', 'gtts', 'mock']),
              help='TTS engine to use')
@click.option('--language', '-l', default='en', help='Language code (e.g., en, es, fr)')
@click.option('--rate', '-r', default=1.0, type=float, help='Speech rate (0.5-2.0)')
@click.option('--volume', '-v', default=1.0, type=float, help='Volume level (0.0-1.0)')
@click.option('--output', '-o', default=None, help='Save to file (e.g., output.mp3)')
def speak(text, engine, language, rate, volume, output):
    """Speak text using text-to-speech"""
    try:
        click.echo(f"{Fore.CYAN}Initializing {engine} engine...{Style.RESET_ALL}")
        
        tts = TextToSpeech(
            engine=engine,
            language=language,
            rate=rate,
            volume=volume
        )
        
        click.echo(f"{Fore.GREEN}Configuration:{Style.RESET_ALL}")
        info = tts.get_info()
        for key, value in info.items():
            click.echo(f"  {key}: {value}")
        
        if output:
            click.echo(f"\n{Fore.YELLOW}Saving to {output}...{Style.RESET_ALL}")
            tts.save_to_file(text, output)
            click.echo(f"{Fore.GREEN}✓ Saved successfully!{Style.RESET_ALL}")
        else:
            click.echo(f"\n{Fore.YELLOW}Speaking...{Style.RESET_ALL}")
            tts.speak(text)
            click.echo(f"{Fore.GREEN}✓ Done!{Style.RESET_ALL}")
    
    except Exception as e:
        click.echo(f"{Fore.RED}Error: {e}{Style.RESET_ALL}", err=True)


@cli.command()
def info():
    """Show TTS tool information"""
    config = Config()
    
    click.echo(f"\n{Fore.CYAN}{'='*50}")
    click.echo(f"Text-to-Speech Tool Information")
    click.echo(f"{'='*50}{Style.RESET_ALL}\n")
    
    click.echo(f"{Fore.GREEN}Default Configuration:{Style.RESET_ALL}")
    click.echo(f"  Engine: {config.get('default_engine')}")
    click.echo(f"  Language: {config.get('default_language')}")
    click.echo(f"  Rate: {config.get('default_rate')}")
    click.echo(f"  Volume: {config.get('default_volume')}")
    
    click.echo(f"\n{Fore.GREEN}Supported Languages:{Style.RESET_ALL}")
    languages = config.get('supported_languages', [])
    click.echo(f"  {', '.join(languages)}")
    
    click.echo(f"\n{Fore.GREEN}Available Engines:{Style.RESET_ALL}")
    click.echo(f"  • pyttsx3 - Offline, cross-platform")
    click.echo(f"  • gtts - Google Text-to-Speech (online)")
    click.echo(f"  • mock - For testing\n")


@cli.command()
@click.argument('config_file', default='config.yaml')
def show_config(config_file):
    """Show configuration file"""
    config = Config(config_file)
    
    click.echo(f"\n{Fore.CYAN}Configuration:{Style.RESET_ALL}\n")
    for key, value in config.config.items():
        click.echo(f"  {key}: {value}")
    click.echo()


if __name__ == '__main__':
    cli()
