# https://click.palletsprojects.com/en/8.0.x/testing/

from click.testing import CliRunner
from pathlib import Path
from rachleff.main import pdf_to_string
from rachleff.constants import DATA_PATH, TEST_YEAR, COMPANY_IN

# TODO: not using only the test year, and then not finding the company
def test_pdf_to_string() -> None:
    runner = CliRunner()
    input = str(Path(DATA_PATH, str(TEST_YEAR)).with_suffix(".pdf"))
    result = runner.invoke(pdf_to_string, [input], standalone_mode=False)
    assert result.exit_code == 0
    assert len(result.return_value) > 0
    assert COMPANY_IN in result.return_value
