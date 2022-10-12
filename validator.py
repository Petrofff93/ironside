from utils import country_mapper
from utils.exceptions import InvalidCountryException, MissingApiKey, MissingData


class Validator:
    @staticmethod
    def validate_input_is_string_and_present(input_data):
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
