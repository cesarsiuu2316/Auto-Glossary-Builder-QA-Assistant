import click


@click.group() # Creates a click command groupd
def cli(): # This is the main entry point for the click application
    pass


@cli.command() # Converts the function into a click command
@click.option('--count', default=1, help='Lists N entries in the glossary.')
def list(count):
    """List N glossary entries."""
    for _ in range(count):
        click.echo("Glossary...")


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