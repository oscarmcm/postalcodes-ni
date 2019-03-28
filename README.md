
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
    get_department_by_iso, get_department_by_postal,
    get_municipality_by_name, get_municipality_by_postal
)
```

This package uses data from those websites:

- [ISO 3166-2:NI](https://es.wikipedia.org/wiki/ISO_3166-2:NI)
- [Postal Codes](https://es.wikipedia.org/wiki/Anexo:C%C3%B3digos_postales_de_Nicaragua)

Usage
--------------

`postalcodes_ni` exposes the following methods:

- `get_department_by_iso` for get all the municipalities in a department using the ISO code - Ex **MN** for **Managua** department.
- `get_department_by_postal` for get all the municipalities in a department using the postal code - Ex **10000** for **Managua** department.
- `get_municipality_by_name` for get an expecific municipality using his name - Ex **Altagracia** for the **Rivas** department.
- `get_municipality_by_postal` for get an expecific municipality using his postal code - Ex **48800** for the municipality of **Altagracia** from **Rivas** department.

Running Tests
--------------

Does the code actually work?

    $ source env/bin/activate
    (env) $ pip install -r requirements_dev.txt
    (env) $ make test-all
