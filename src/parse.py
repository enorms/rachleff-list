# import pdfbox
import codecs
from pathlib import Path
import urllib.request
from constants import DATA_PATH, LIST_2019

# p = pdfbox.PDFBox()


def get_data(debug: bool = False, verbose: bool = False) -> Path:
    fp = urllib.request.urlopen(LIST_2019)
    mybytes = fp.read()
    fp.close()
    # # mystr = mybytes.decode("utf8")
    Path(DATA_PATH).mkdir(exist_ok=True)
    p = Path("./_data/1")
    p.write_bytes(mybytes)
    return p


def pdf_to_string() -> any:
    datafile = open(DATA_PATH + "1", "rb")
    pdfdatab = datafile.read()  # this is binary data
    datafile.close()

    b64PDF = codecs.encode(pdfdatab, "base64")
    Sb64PDF = b64PDF.decode("utf-8")
    return Sb64PDF
