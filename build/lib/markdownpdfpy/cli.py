"""Console script for markdownpdfpy."""
import sys
import click


@click.command()
@click.argument('file')
def main(args=None):
    """Console script for markdownpdfpy."""
    click.echo("Replace this message by putting your code into "
               "markdownpdfpy.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
