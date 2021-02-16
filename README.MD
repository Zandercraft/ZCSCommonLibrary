# ZCSCommonLibrary

---
A Common Library For Use In Computer Science Projects

**PIP Package**: zcscommonlib <br />
**Current Version:** 0.1.0 <br />
**License**: Mozilla Public License Version 2.0

### Build The Library
Prepare the library for development and build it.
```commandline
pip install -r requirements.txt
python setup.py bdist_wheel
pip install ./dist/zcscommonlib-VERSION-py3-none-any.whl
```

### Running Tests
Run tests on the functions listed in `test_functions.py`.
```commandline
python setup.py pytest
```

# Contents
Below is the documentation for all the functions available in the library.

## Functions Module

---
Currently the only module, provides all functions in the library.
### Haversine - functions.haversine()
#### Purpose 
Calculates the great circle distance between two points on the
earth (specified in decimal degrees), returns the distance in
meters.

#### Args (In order)
lon1 (float): The longitude of the first point.<br />
lat1: (float): The latitude of the first point.<br />
lon2: (float): The longitude of the second point.<br />
lat2: (float): The latitude of the second point.<br />

#### Returns
The distance in meters between the two sets of coordinates.

### Month - functions.month()
#### Purpose 
Takes an input of an integer and returns a string of the month of that number.

#### Args
num (int): The number of the month.

#### Returns
The month's name in string format.
