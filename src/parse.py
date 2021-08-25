import pdfbox
import codecs
from pathlib import Path
import re
import urllib.request
from constants import DATA_PATH, TEST_YEAR, COMPANY_IN_2019, STATE_CODES
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
    """Given the path of pdf input file,
    returns contents in a string.

    Returns: string using casefold
    """
    pdf_ref = pdfbox.PDFBox()
    input_path = Path(input).with_suffix(".pdf")
    pdf_ref.extract_text(str(input_path))  # -> p.filename.txt
    output = Path(input).with_suffix(".txt")
    txt = output.read_text(errors="ignore")  # pdfs have non text byte data
    txt = txt.casefold()
    return txt


known_companies = [
    "act-on software",
    "arctic wolf networks",
    "avi networks",
    "big switch networks",
    "blue jeans network",
    "bustle digital group",
    "carbon",
]

# TODO: get company names from string
def extract_companies_(test: bool) -> list[str]:
    years = [TEST_YEAR] if test else [2019, 2018]
    new_lines = []
    for datum in data:
        if datum.year in years:
            input = Path(DATA_PATH, str(datum.year)).with_suffix(".txt")
            txt = input.read_text(errors="ignore")  # pdfs have non text byte data
            txt = txt.lower()
            txt = txt.encode("ascii", "ignore").decode()
            lines = re.split("\n+", txt)
            past_header = False
            line_counter = 0
            for line in lines:
                if (
                    not len(line) <= 1
                    and not len(re.split(" |-", line))
                    >= 5  # descriptions longer than names
                    and not re.search("\w+,/w+", line)  # city, state | description
                    and not re.search("career.?launching", line)  # specific wording
                    and not re.search("companies list", line)
                    and not re.search("\d\s+edition", line)
                    and not re.search("\w+\.com|\.net|\.io|\.ai|\.co|.us|.info", line)
                    # and not re.search(
                    #     "[a-zA-Z]+,\s+az|ca|co|dc|ga|id|il|ma|md|mi|nc|ny|oh|or|tx|ut|wa\s?",
                    #     line,
                    # ) # missed: 'atlanta, ga'
                    and not re.search(",", line)
                    and not re.search("atlanta, ga", line)
                    # and not True in [code in line for code in STATE_CODES]
                ):
                    new_lines.append(line)
    # add known missing companies
    [new_lines.append(company) for company in known_companies]
    new_lines.sort()
    return new_lines


# TODO: don't print this error
#     Aug 25, 2021 1:24:08 AM org.apache.pdfbox.pdmodel.font.PDSimpleFont toUnicodeWARNING: No Unicode mapping for f_f (31) in font QSPMMV+Calibre-Regular
def company_in_year_(company: str, test: bool) -> list[str]:
    """Return true if the company in any year
    else false"""
    # test with one year
    found_in = []
    years = [TEST_YEAR] if test else [2019, 2018]
    for datum in data:
        if datum.year in years:
            input = Path(DATA_PATH, str(datum.year)).with_suffix(".pdf")
            txt = pdf_to_string_(str(input))
            if company in txt:
                found_in.append(str(datum.year))
    return found_in
