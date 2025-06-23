import click
import json
import os
from Levenshtein import distance
import numpy as np


GLOSSARY_PATH = "glossary.json"  # Path to the glossary JSON file
GLOSSARY_DICT = {}  # Dictionary to hold the glossary entries


@click.group() # Creates a click command groupd
def cli(): # This is the main entry point for the click application
    """Glossary CLI Tool."""
    global GLOSSARY_DICT
    if os.path.exists(GLOSSARY_PATH):
        with open(GLOSSARY_PATH, 'r') as f:
            GLOSSARY_DICT = json.load(f)
            GLOSSARY_DICT = GLOSSARY_DICT.get("Glossary", {})
    pass


@cli.command() # Converts the function into a click command
@click.option('--count', default=10, help='Lists N entries in the glossary.')
def listw(count):
    """List N glossary entries."""
    if not GLOSSARY_DICT:
        click.echo("No glossary entries found.")
        return
    # Get the entries from the glossary dictionary
    entries = list(sorted(GLOSSARY_DICT.items()))[:count]
    # Print the header
    click.echo(f"{'Term':<45} {'# of Variants'}")
    click.echo("-" * 60)
    # Print each entry with its term and number of variants
    for term, value in entries:
        variant_count = len(value.get('variants', []))
        click.echo(f"{term:<45} {variant_count}")


@cli.command() # Converts the function into a click command
@click.argument('word') # This is a command that takes an argument
def define(word):
    """Define WORD in glossary."""
    click.echo(
        f"Canonical: {word}\n"
        f"Definition: {GLOSSARY_DICT[word]['definition'] if word in GLOSSARY_DICT else 'Not found'}\n"
        f"Example: {GLOSSARY_DICT[word]['example'] if word in GLOSSARY_DICT else 'Not found'}"
    )


@cli.command() # Converts the function into a click command
@click.argument('words', nargs=-1) # This is a command that takes an argument
def search(words):
    """Search WORD in glossary."""
    word = ""
    for w in words:
        word += w + " "
    distances = []
    for i in range(len(GLOSSARY_DICT)):
        term = list(GLOSSARY_DICT.keys())[i]
        dist = distance(word, term)
        distances.append(dist)
    match = np.argmin(distances)
    closest_term = list(GLOSSARY_DICT.keys())[match]
    click.echo(
        f"Closest match: {closest_term if closest_term == word else f'{closest_term}'}"
    )


if __name__ == "__main__":
    cli()