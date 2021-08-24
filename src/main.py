# Starter program with click cli examples

import click
from pathlib import Path
from parse import get_data, pdf_to_string


# Shared args
@click.group()
@click.option("--debug", "-d", is_flag=True, help="Use debug mode")
@click.option("--verbose", "-v", is_flag=True, help="Use verbose mode")
def cli(debug: bool, verbose: bool) -> None:
    click.echo("Debug mode is on") if debug else None
    click.echo("Verbose mode is on") if verbose else None


@cli.command()
@click.pass_context
def get_data_(ctx: click.Context) -> Path:
    res: Path = ctx.invoke(get_data)
    return res


@cli.command()
@click.pass_context
def pdf_to_string_(ctx: click.Context) -> Path:
    res: Path = ctx.invoke(pdf_to_string)
    return res


if __name__ == "__main__":
    cli()
