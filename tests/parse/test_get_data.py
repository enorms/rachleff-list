# https://click.palletsprojects.com/en/8.0.x/testing/

from pathlib import Path
from click.testing import CliRunner
from src.main import get_data_


def test_get_data():
    runner = CliRunner()
    result = runner.invoke(get_data_)
    assert result.exit_code == 0
    p = Path("./_data/1")
    assert len(p.read_bytes()) > 0
