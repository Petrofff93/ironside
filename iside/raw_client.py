from datetime import datetime
from typing import Optional
import aiohttp

from iside.area import Area
from utils.exceptions import AccessDeniedException
from utils.timefilter import time_filter
from validator import Validator


class IsideRawClient:
    """Client to perform API calls and return JSON data for ALSI API: https://alsi.gie.eu/#/api"""

    BASE_URL = "https://agsi.gie.eu/api"

    def __init__(self, api_key, session: Optional[aiohttp.ClientSession] = None):
        self.api_key = api_key
        self.session = session

        if not self.session:
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
        facility_code,
        company_code,
        country_code,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        limit: Optional[int] = 0,
    ):
        timefilter = time_filter(start, end, limit)

        return await self.__base_request(
            facility_code, company_code, country_code, timefilter=timefilter
        )

    async def __base_request(self, *path_segments: str, timefilter: time_filter):

        # Validator.check_if_valid_time_filter(timefilter)

        params = {}

        if any(timefilter):
            start, end, limit = timefilter
            if start:
                params["from"] = start.strftime("%Y-%m-%d")
            if end:
                params["till"] = end.strftime("%Y-%m-%d")
            if limit:
                params["limit"] = str(limit)

        url = f"{self.BASE_URL}/{'/'.join(path_segments)}"

        async with self.session.get(url, params=params) as resp:
            if resp.status < 400:
                if "access denied" in (await resp.text()):
                    raise AccessDeniedException("Check if API key is invalid.")
                return await resp.json()

    async def close_session(self):
        """Close the session."""
        if self.session:
            await self.session.close()
