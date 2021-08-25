# https://click.palletsprojects.com/en/8.0.x/testing/

from pathlib import Path
from click.testing import CliRunner

# from main import get_data
from main import get_data
from constants import DATA_PATH, TEST_YEAR
from data import data_2019


def test_get_data() -> None:
    """Use optional argument to grab only one year."""
    runner = CliRunner()
    # standalone_mode=False gives the return_value
    result = runner.invoke(get_data, ["--test"], standalone_mode=False)
    assert result.exit_code == 0
    assert len(result.return_value.read_bytes()) > 0


if __name__ == "__main__":
    test_get_data()
