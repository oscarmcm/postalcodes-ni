import pytest

from postalcodes_ni import (
    get_department_by_iso, get_department_by_postal,
    get_municipality_by_name, get_municipality_by_postal
)
from postalcodes_ni.exceptions import ISOCodeError, PostalCodeError


def test_get_department_by_iso():
    """ Test get all the municipalities from a department by iso code
    """
    with pytest.raises(ISOCodeError):
        get_department_by_iso('WRONG')
    mn = get_department_by_iso('MN')
    assert isinstance(mn, list)
    assert len(mn) > 0


def test_get_department_by_postal():
    """ Test get all the municipalities from a department by postal code
    """
    with pytest.raises(PostalCodeError):
        get_department_by_postal(666)
    mn = get_department_by_postal(10000)
    assert isinstance(mn, list)
    assert len(mn) > 0


def test_get_municipality_by_name():
    """ Test get a municipality from his name
    """
    with pytest.raises(PostalCodeError):
        get_municipality_by_name('WRONG')
    mn = get_municipality_by_name('centro historico cultural')
    assert isinstance(mn, dict)
    assert len(mn.keys()) == 3


def test_get_municipality_by_postal():
    """ Test get a municipality from his postal code
    """
    with pytest.raises(PostalCodeError):
        get_municipality_by_postal(666)
    mn = get_municipality_by_postal(11001)
    assert isinstance(mn, dict)
    assert len(mn.keys()) == 3


def test_all():
    """ Test that __all__ contains only names that are actually exported.
    """
    import postalcodes_ni

    missing = set(n for n in postalcodes_ni.__all__
                  if getattr(postalcodes_ni, n, None) is None)
    assert len(missing) == 0
