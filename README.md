
postalcodes-ni
==============

Python package for handle Nicaragua postal codes

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-python](https://img.shields.io/pypi/pyversions/postalcodes_ni.svg)](https://pypi.org/project/postalcodes_ni/)
[![PyPI version](https://badge.fury.io/py/postalcodes-ni.svg)](https://badge.fury.io/py/postalcodes-ni)
[![Travis-ci](https://travis-ci.org/oscarmcm/postalcodes-ni.png?branch=master)](https://travis-ci.org/oscarmcm/postalcodes-ni)
[![GitHub version](https://badge.fury.io/gh/oscarmcm%2Fpostalcodes-ni.svg)](https://badge.fury.io/gh/oscarmcm%2Fpostalcodes-ni)
[![Documentation Status](https://readthedocs.org/projects/postalcodes-ni/badge/?version=latest)](http://postalcodes-ni.readthedocs.io/?badge=latest)

Quickstart
----------
Install `postalcodes-ni`:

    $ pip install postalcodes-ni

Then use it in your project:

```python
from postalcodes_ni import (
    get_all_municipalities_by_iso, get_all_municipalities_by_postal,
    get_municipality_by_name, get_municipality_by_postal
)
```

You can find the documentation in [https://postalcodes-ni.readthedocs.io](https://postalcodes-ni.readthedocs.io/en/latest/)

This package uses data from those websites:

- [ISO 3166-2:NI](https://es.wikipedia.org/wiki/ISO_3166-2:NI)
- [Postal Codes](https://es.wikipedia.org/wiki/Anexo:C%C3%B3digos_postales_de_Nicaragua)

Usage
--------------

`postalcodes_ni` exposes the following methods:

- `get_all_municipalities_by_iso` for get all the municipalities in a department using the ISO code - Ex **MN** for **Managua** department.
- `get_all_municipalities_by_postal` for get all the municipalities in a department using the postal code - Ex **10000** for **Managua** department.
- `get_municipality_by_name` for get an specific municipality using his name - Ex **Altagracia** for the **Rivas** department.
- `get_municipality_by_postal` for get an specific municipality using his postal code - Ex **48800** for the municipality of **Altagracia** from **Rivas** department.

Example
--------------

First, you need import the methods that you want to use

```python
from postalcodes_ni import (
    get_all_municipalities_by_iso, get_all_municipalities_by_postal,
    get_municipality_by_name, get_municipality_by_postal
)
```

For get all the municipalities in a department use the following methods

```python
>>> # Get all the municipalities in Carazo department using iso code
>>> get_all_municipalities_by_iso('CA')
[('Jinotepe', 45000), ('Dolores', 46100), ('El Rosario', 46200), ...]

>>> # Get all the municipalities in Carazo department using postal code
>>> get_all_municipalities_by_postal(45000)
[('Jinotepe', 45000), ('Dolores', 46100), ('El Rosario', 46200), ...]
```

For get an specific municipality in a department use the following methods

```python
>>> # Get a municipality using his name
>>> get_municipality_by_name('nindiri')
('Nindirí', 42200)

>>> # Get a municipality using his postal code
>>> get_municipality_by_postal(42500)
('Catarina', 42500)
```

Running Tests
--------------

Does the code actually work?

    $ source env/bin/activate
    (env) $ pip install -r requirements_dev.txt
    (env) $ make test-all
