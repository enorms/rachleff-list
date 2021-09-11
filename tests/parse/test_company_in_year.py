# https://click.palletsprojects.com/en/8.0.x/testing/

from click.testing import CliRunner
from pathlib import Path
import re
from main import check
from constants import DATA_PATH, TEST_YEAR, COMPANY_IN, COMPANY_NOT_IN


def test_company_in_year() -> None:
    runner = CliRunner()

    # expect true
    result = runner.invoke(check, [COMPANY_IN, "--test"], standalone_mode=False)
    assert result.exit_code == 0
    assert re.search(r"\d+", str(result.return_value))  # year of list
    # expect false
    result = runner.invoke(check, [COMPANY_NOT_IN, "--test"], standalone_mode=False)
    assert result.exit_code == 0
    assert not re.search(r"\d", str(result.return_value))  # no years
