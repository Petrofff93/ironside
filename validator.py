from datetime import datetime

from utils import country_mapper
from utils.exceptions import (
    InvalidCountryException,
    MissingApiKey,
    MissingData,
    InvalidTimeFilter,
)


class Validator:
    @staticmethod
    def validate_country_code_is_string_and_present(input_data):
        if not input_data:
            raise MissingData("There is missing input data, please check again!")
        if isinstance(input_data, str) and input_data.upper() in country_mapper.mapper:
            return input_data

        if input_data not in country_mapper.mapper:
            raise InvalidCountryException(
                "The country you're looking for is not supported. Please contact us!"
            )
        else:
            raise TypeError("The input data must be of type string!")

    @staticmethod
    def check_if_apy_key_provided(input_data):
        if input_data:
            return input_data
        raise MissingApiKey("Your API KEY is missing!")

    @staticmethod
    def check_if_valid_time_filter(timefilter: tuple):
        start, end, limit = timefilter

        if (
            len(timefilter) <= 3
            and (limit and (isinstance(limit, int) and limit > 0))
            and ((start and end) and (start < end))
            and (start and (isinstance(start, datetime)))
            and (end and (isinstance(end, datetime)))
        ):
            return timefilter

        raise InvalidTimeFilter("Invalid time filter!")

    @staticmethod
    def validate_company_code_facility_code_are_present(input_data):
        if not input_data:
            raise MissingData("There is missing input data, please check again!")

        return input_data
