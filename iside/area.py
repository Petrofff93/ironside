from validator import Validator


class Area:
    def __init__(self, country_code: str, company_code: str, facility_code: str):
        self.country_code = country_code
        self.company_code = company_code
        self.facility_code = facility_code

    @property
    def country_code(self):
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = Validator.validate_country_code_is_string_and_present(value)

    @property
    def company_code(self):
        return self.__company_code

    @company_code.setter
    def company_code(self, value):
        self.__company_code = Validator.validate_company_code_facility_code_are_present(value)

    @property
    def facility_code(self):
        return self.__facility_code

    @facility_code.setter
    def facility_code(self, value):
        self.__facility_code = Validator.validate_company_code_facility_code_are_present(value)
