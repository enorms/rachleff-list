# import pdfbox
import codecs
from pathlib import Path
import urllib.request
from constants import DATA_PATH, TEST_YEAR
from data import Source_Data, data

# p = pdfbox.PDFBox()


def get_data_(test: bool) -> Path:
    Path(DATA_PATH).mkdir(exist_ok=True)
    # test with one year
    years = [TEST_YEAR] if test else [2019, 2018]
    for datum in data:
        if datum.year in years:
            fp = urllib.request.urlopen(datum.url)
            mybytes = fp.read()
            fp.close()
            # # mystr = mybytes.decode("utf8")
            path = Path(DATA_PATH, str(datum.year))
            path.write_bytes(mybytes)
    return path


def pdf_to_string() -> str:
    datafile = open(DATA_PATH + "1", "rb")
    pdfdatab = datafile.read()  # this is binary data
    datafile.close()

    b64PDF = codecs.encode(pdfdatab, "base64")
    Sb64PDF = b64PDF.decode("utf-8")
    return Sb64PDF
