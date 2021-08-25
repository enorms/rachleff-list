# https://click.palletsprojects.com/en/8.0.x/testing/

from click.testing import CliRunner
from pathlib import Path
from main import pdf_to_string
from constants import DATA_PATH, TEST_YEAR, KNOWN_COMPANY_IN_2019_LIST


def test_pdf_to_string() -> None:
    runner = CliRunner()
    input = str(Path(DATA_PATH, str(TEST_YEAR)).with_suffix(".pdf"))
    result = runner.invoke(pdf_to_string, [input], standalone_mode=False)
    assert result.exit_code == 0
    assert len(result.return_value) > 0
    assert KNOWN_COMPANY_IN_2019_LIST in result.return_value
