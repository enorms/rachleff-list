#!/usr/bin/env python3

# Implementation of the CLI interface

# Allow relative import from anywhere
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import click
from pathlib import Path
from rachleff.parse import check_dropped, get_data_, pdf_to_string_, check_years
from rachleff.data import data, Source_Data

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
    """Download source data from internet and save to disk
    as pdf file in bytes.

    Param
        Year is an optional param used for testing, to only get from 1 data source.
    """
    res = ctx.invoke(get_data_, test)
    return res


@cli.command()
@click.pass_context
@click.argument("input", type=str)
def pdf_to_string(ctx: click.Context, input: str) -> str:
    """Convert saved pdfs to text"""
    return ctx.invoke(pdf_to_string_, input)


@cli.command()
@click.pass_context
# @click.option("--input", "-i", is_flag=False, help="Test with only one year", type=str)
def update(ctx: click.Context, input: str = "", test: bool = False) -> None:
    """Download and convert to text.

    Param
        Year is an optional param used for testing, to only get from 1 data source.
    """
    ctx.invoke(get_data_, test)
    ctx.invoke(pdf_to_string_, input)


@cli.command()
@click.pass_context
@click.option(
    "--test", "-t", is_flag=True, default=False, help="Test with only one year"
)
@click.argument("company", type=str)
def check(ctx: click.Context, company: str, test: bool) -> tuple:
    """Use expected data paths to load text files,
    and return just the company names with the years"""

    company = company.casefold()

    # check years
    years_found = ctx.invoke(check_years, company, test)
    if years_found:
        click.echo(f"{company.title()} found in years {years_found}")
    else:
        click.echo(f"{company.title()} not found")

    # check dropped
    dropped = ctx.invoke(check_dropped, company, test)
    if dropped:
        click.echo(f"Dropped due to: {dropped}")

    return (years_found, dropped)


if __name__ == "__main__":
    cli()
