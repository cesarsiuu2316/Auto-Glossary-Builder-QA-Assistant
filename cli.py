import click
import json
import os


GLOSSARY_PATH = "glossary.json"  # Path to the glossary JSON file
GLOSSARY_DICT = {}  # Dictionary to hold the glossary entries


@click.group() # Creates a click command groupd
def cli(): # This is the main entry point for the click application
    """Glossary CLI Tool."""
    global GLOSSARY_DICT
    if os.path.exists(GLOSSARY_PATH):
        with open(GLOSSARY_PATH, 'r') as f:
            GLOSSARY_DICT = json.load(f)
    pass


@cli.command() # Converts the function into a click command
@click.option('--count', default=10, help='Lists N entries in the glossary.')
def list(count):
    """List N glossary entries."""
    if not GLOSSARY_DICT:
        click.echo("No glossary entries found.")
        return
    else:
        entries = list(GLOSSARY_DICT.get("Glossary", {}).items())[:count]
        for term, value in entries:
            click.echo(f"{term}:\t{len(value.get("variants", []))} variants")


@cli.command() # Converts the function into a click command
@click.argument('word') # This is a command that takes an argument
def define(word):
    """Define WORD in glossary."""
    click.echo(f"Defining: {word}")


@cli.command() # Converts the function into a click command
@click.argument('word') # This is a command that takes an argument
def search(word):
    """Search WORD in glossary."""
    click.echo(f"Searching for: {word}")


if __name__ == "__main__":
    cli()