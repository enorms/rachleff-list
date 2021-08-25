import pdfbox
import codecs
from pathlib import Path
import urllib.request
from constants import DATA_PATH, TEST_YEAR
from data import Source_Data, data


def get_data_(test: bool) -> Path:
    """Save as pdf file(s)"""
    Path(DATA_PATH).mkdir(exist_ok=True)
    # test with one year
    years = [TEST_YEAR] if test else [2019, 2018]
    for datum in data:
        if datum.year in years:
            fp = urllib.request.urlopen(datum.url)
            mybytes = fp.read()
            fp.close()
            path = Path(DATA_PATH, str(datum.year)).with_suffix(".pdf")  # pdf in bytes
            path.write_bytes(mybytes)
    return path


def pdf_to_string_(input: str) -> str:
    """Reads pdf into string"""
    pdf_ref = pdfbox.PDFBox()
    input_path = Path(input).with_suffix(".pdf")
    pdf_ref.extract_text(str(input_path))  # -> p.filename.txt
    output = Path(input).with_suffix(".txt")
    txt = output.read_text(errors="ignore")  # pdfs have non text byte data
    return txt
