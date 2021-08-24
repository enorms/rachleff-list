from pathlib import Path
import urllib.request
from constants import DATA_PATH, LIST_2019


def get_data(debug: bool = False, verbose: bool = False) -> Path:
    fp = urllib.request.urlopen(LIST_2019)
    mybytes = fp.read()
    fp.close()
    # # mystr = mybytes.decode("utf8")
    Path(DATA_PATH).mkdir(exist_ok=True)
    p = Path("./_data/1")
    p.write_bytes(mybytes)
    return p
