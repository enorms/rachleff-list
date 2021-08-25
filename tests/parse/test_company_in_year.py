# https://click.palletsprojects.com/en/8.0.x/testing/

from click.testing import CliRunner
from pathlib import Path
import re
from main import company_in_year
from constants import DATA_PATH, TEST_YEAR, COMPANY_IN_2019, COMPANY_NOT_IN_2019


def test_company_in_year() -> None:
    runner = CliRunner()

    # expect true
    result = runner.invoke(
        company_in_year, [COMPANY_IN_2019, "--test"], standalone_mode=False
    )
    assert result.exit_code == 0
    assert re.search(r"\d+", str(result.return_value))  # year of list
    # expect false
    result = runner.invoke(
        company_in_year, [COMPANY_NOT_IN_2019, "--test"], standalone_mode=False
    )
    assert result.exit_code == 0
    assert not re.search(r"\d", str(result.return_value))  # no years
