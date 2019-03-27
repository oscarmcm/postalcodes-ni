import unicodedata

from ._codes import _postal_codes as postal_codes
from .exceptions import ISOCodeError, PostalCodeError


def get_department_by_iso(iso_code: str) -> list:
    """ Returns all the records for a department based on the ISO code
    """
    iso_code = iso_code.upper()
    if iso_code not in postal_codes:
        raise ISOCodeError(
            f'Incorrect ISO 3166-2 code \n The code {iso_code} doesnt exists'
        )

    return postal_codes.get(iso_code)


def get_department_by_postal(postal_code: int) -> list:
    """ Returns all the records for a department based on the postal code
    """
    department_key = None
    for department, municipalities  in postal_codes.items():
        for municipality in municipalities:
            if (
                municipality['code'] == postal_code
                and municipality['neighborhood'] == 'master'
            ):
                department_key = department
                break
    if department_key is None:
        raise PostalCodeError(
            f'Cant find any department with the code {postal_code}'
        )

    return postal_codes.get(department_key)


def get_municipality_by_name(name: str) -> dict:
    """ Returns a single record for a municipality based on the name
    """

    def strip_accents(s):
        return ''.join(
            c
            for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn'
        )

    name = strip_accents(name).title()
    department_key = None
    municipality_key = None
    for department, municipalities in postal_codes.items():
        for index, municipality in enumerate(municipalities):
            if strip_accents(municipality['municipality']) == name:
                department_key = department
                municipality_key = index
                break
            if strip_accents(municipality['neighborhood']) == name:
                department_key = department
                municipality_key = index
                break

    if department_key is None and municipality_key is None:
        raise PostalCodeError(
            f'Cant find any municipality with the name {name}'
        )

    return postal_codes.get(department_key)[municipality_key]


def get_municipality_by_postal(postal_code: int) -> dict:
    """ Returns a single record for a municipality based on the postal code
    """
    for department, municipalities in postal_codes.items():
        for index, municipality in enumerate(municipalities):
            if municipality['code'] == postal_code:
                return postal_codes[department][index]

    raise PostalCodeError(
        f'Cant find any municipality with the code {postal_code}'
    )
