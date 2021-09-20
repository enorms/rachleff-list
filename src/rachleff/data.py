# Handle source web data

from datetime import datetime
import pydantic
from pydantic import BaseModel, NoneStr

# Allow relative import from anywhere
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class Source_Data(BaseModel):
    year: int
    url: str


# 2021 scraped as no pdf yet
data = [
    Source_Data(
        year=2021,
        url="",
    ),
    Source_Data(
        year=2020,
        url="https://cdn.wealthfront.com/public.email.images/2020_Career-Launching_List_vF.pdf",
    ),
    Source_Data(
        year=2019,
        url="https://blog.wealthfront.com/wp-content/uploads/2019/12/2019-Career-Launching-List-2.pdf",
    ),
    Source_Data(
        year=2018,
        url="https://blog.wealthfront.com/wp-content/uploads/2018/10/2018_Career-Launching_List-10.pdf",
    ),
    Source_Data(
        year=2017,
        url="https://cdn.wealthfront.com/public.email.images/WF-2017-CareerGuide.pdf",
    ),
    Source_Data(
        year=2016,
        url="https://cdn.wealthfront.com/public.email.images/WF-2016-CareerGuide.pdf",
    ),
    Source_Data(
        year=2015,
        url="https://cdn.wealthfront.com/public.email.images/WF-2015-CareerGuide.pdf",
    ),
]
