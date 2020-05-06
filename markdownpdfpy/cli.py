"""Console script for markdownpdfpy."""
import sys
import click
from markdownpdfpy import markdownToHTML


@click.command()
@click.argument("filename", required=True)
def main(filename):
    """Console script for markdownpdfpy."""
    markdownToHTML(filename)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
