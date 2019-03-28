import pytest

from postalcodes_ni import (
    get_all_municipalities_by_iso,
    get_all_municipalities_by_postal,
    get_municipality_by_name,
    get_municipality_by_postal,
)
from postalcodes_ni.exceptions import ISOCodeError, PostalCodeError


def test_get_all_municipalities_by_iso():
    """ Test get all the municipalities from a department by iso code
    """
    with pytest.raises(ISOCodeError):
        get_all_municipalities_by_iso('WRONG')
    mn = get_all_municipalities_by_iso('MN')
    assert isinstance(mn, list)
    assert isinstance(mn[0], tuple)
    assert len(mn) > 0


def test_get_all_municipalities_by_postal():
    """ Test get all the municipalities from a department by postal code
    """
    with pytest.raises(PostalCodeError):
        get_all_municipalities_by_postal(666)
    mn = get_all_municipalities_by_postal(10000)
    assert isinstance(mn, list)
    assert isinstance(mn[0], tuple)
    assert len(mn) > 0


def test_get_municipality_by_name():
    """ Test get a municipality from his name
    """
    with pytest.raises(PostalCodeError):
        get_municipality_by_name('WRONG')
    # Search by neighborhood name
    mn = get_municipality_by_name('centro historico cultural')
    assert isinstance(mn, tuple)
    assert isinstance(mn[0], str)
    assert isinstance(mn[1], int)
    assert mn[1] == 11001
    assert len(mn) == 2
    # Search by municipality name
    mn = get_municipality_by_name('San Carlos')
    assert isinstance(mn, tuple)
    assert isinstance(mn[0], str)
    assert isinstance(mn[1], int)
    assert len(mn) == 2
    assert mn[1] == 91000


def test_get_municipality_by_postal():
    """ Test get a municipality from his postal code
    """
    with pytest.raises(PostalCodeError):
        get_municipality_by_postal(666)
    mn = get_municipality_by_postal(11001)
    assert isinstance(mn, tuple)
    assert isinstance(mn[0], str)
    assert isinstance(mn[1], int)
    assert len(mn) == 2


def test_all():
    """ Test that __all__ contains only names that are actually exported.
    """
    import postalcodes_ni

    missing = set(
        n
        for n in postalcodes_ni.__all__
        if getattr(postalcodes_ni, n, None) is None
    )
    assert len(missing) == 0
