# Starter program with click cli examples

import click
from pathlib import Path
from parse import get_data_, pdf_to_string
from data import data
from data import Source_Data

# Shared args
@click.group()
@click.option("--debug", "-d", is_flag=True, default=False, help="Use debug mode")
@click.option("--verbose", "-v", is_flag=True, default=False, help="Use verbose mode")
def cli(debug: bool, verbose: bool) -> None:
    click.echo("Debug mode is on") if debug else None
    click.echo("Verbose mode is on") if verbose else None


@cli.command()
@click.pass_context
@click.option(
    "--test", "-t", is_flag=True, default=False, help="Test with only one year"
)
def get_data(ctx: click.Context, test: bool) -> Path:
    """Download source data from internet and save to disk.

    Param
        Year is an optional param used for testing, to only get from 1 data source.
    """
    res = ctx.invoke(get_data_, test)
    return res


# @cli.command()
# @click.pass_context
# def pdf_to_string_(
#     ctx: click.Context,
#     source_data: Source_Data = data,
#     debug: bool = False,
#     verbose: bool = False,
# ) -> any:
#     """Take local data and make usable."""
#     return ctx.invoke(pdf_to_string, [source_data, debug, verbose])


if __name__ == "__main__":
    cli()
