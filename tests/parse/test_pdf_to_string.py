# https://click.palletsprojects.com/en/8.0.x/testing/

from pathlib import Path
from click.testing import CliRunner
from src.main import pdf_to_string_


def test_pdf_to_string() -> None:
    runner = CliRunner()
    result = runner.invoke(pdf_to_string_)
    assert result.exit_code == 0
