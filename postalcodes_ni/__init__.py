# -*- coding: utf-8 -*-

"""Top-level package for postalcodes-ni."""
from postalcodes_ni.postalcodes import (
    get_all_municipalities_by_iso, get_all_municipalities_by_postal,
    get_municipality_by_name, get_municipality_by_postal
)
__all__ = [
    'get_all_municipalities_by_iso',
    'get_all_municipalities_by_postal',
    'get_municipality_by_name',
    'get_municipality_by_postal'
]

__author__ = """Oscar Cortez"""
__email__ = 'om.cortez.2010@gmail.com'
__version__ = '1.2.0'
