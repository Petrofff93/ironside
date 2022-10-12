from utils import country_mapper
from utils.exceptions import InvalidCountryException


class Validator:
    
    @staticmethod
    def validate_input_is_string_and_present(input_data):
        if isinstance(input_data, str) and input_data.upper() in country_mapper.mapper:
            return input_data
        
        if input_data not in country_mapper.mapper:
            raise InvalidCountryException("The country you're looking for is not supported. Please contact us!")
        else:
            raise TypeError("The input data must be of type string!")
        
        