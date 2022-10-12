from datetime import datetime
from typing import Optional
import aiohttp

from iside.area import Area
from validator import Validator


class IsideRawClient:
    """Client to perform API calls and return JSON data for ALSI API: https://alsi.gie.eu/#/api"""

    BASE_URL = "https://alsi.gie.eu/api/data/"

    def __init__(self, api_key, session: Optional[aiohttp.ClientSession] = None):
        self.api_key = api_key
        self.session = session

        if self.session:
            self.session = aiohttp.ClientSession(
                raise_for_status=True, headers={"x-key": self.api_key}
            )

    @property
    def api_key(self):
        return self.__api_key

    @api_key.setter
    def api_key(self, value):
        self.__api_key = Validator.check_if_apy_key_provided(value)

    async def query_data_for_facility(
        self,
        facility_code: Area.facility_code,
        company_code: Area.company_code,
        country_code: Area.country_code,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        limit: Optional[int] = 0,
    ):
        pass
