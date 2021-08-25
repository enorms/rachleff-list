# https://click.palletsprojects.com/en/8.0.x/testing/

from click.testing import CliRunner
from pathlib import Path
from main import extract_companies
from constants import DATA_PATH, TEST_YEAR, COMPANY_IN_2019


def test_extract_companies_() -> None:
    runner = CliRunner()
    input = str(Path(DATA_PATH, str(TEST_YEAR)).with_suffix(".txt"))
    result = runner.invoke(extract_companies, ["--test"], standalone_mode=False)
    assert result.exit_code == 0
    assert len(result.return_value) > 0
    assert COMPANY_IN_2019 in result.return_value
