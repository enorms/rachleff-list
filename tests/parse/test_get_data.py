# https://click.palletsprojects.com/en/8.0.x/testing/

from pathlib import Path
from click.testing import CliRunner

# from main import get_data
from main import get_data
from constants import DATA_PATH, TEST_YEAR
from data import data_2019

KNOWN_COMPANY_IN_2019_LIST = "HackerOne"  # after getting string


def test_get_data() -> None:
    """Use optional argument to grab only one year."""
    runner = CliRunner()
    result = runner.invoke(get_data, ["--test"])
    assert result.exit_code == 0
    p = Path(DATA_PATH, str(TEST_YEAR))
    assert len(p.read_bytes()) > 0


if __name__ == "__main__":
    test_get_data()
