# Handle source web data

from datetime import datetime
import pydantic
from pydantic import BaseModel, NoneStr


class Source_Data(BaseModel):
    year: int
    url: str
    date_saved: datetime = datetime.now()


data_2019 = Source_Data(
    year=2019,
    url="https://blog.wealthfront.com/wp-content/uploads/2019/12/2019-Career-Launching-List-2.pdf",
    date_saved=datetime(2021, 8, 24),
)

data_2018 = Source_Data(
    year=2018,
    url="https://blog.wealthfront.com/wp-content/uploads/2019/12/2019-Career-Launching-List-2.pdf",
    date_saved=datetime(2021, 8, 24),
)

data = [data_2019, data_2018]
