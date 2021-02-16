## Welcome to the ZCSCommonLibrary website!

The ZCSCommonLib library exists as a general library to provide various utilities, generally useful in computer science courses. All are welcome to contribute to the library (through pull requests) and add general (or more complicated) functions to it.

### Importing The Library

You can use the following code to import the ZCSCommonLib library to your Python projects.

```python
from zcscommonlib import functions as fcns
```

For more details on how to use the library, see our [documentation here](https://github.com/Zandercraft/ZCSCommonLibrary/wiki).

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

### Support or Contact

Having trouble with using ZCSCommonLibrary? Check out our [documentation](https://github.com/Zandercraft/ZCSCommonLibrary/wiki) or [make a bug report on Github](https://github.com/Zandercraft/ZCSCommonLibrary/issues/new/choose) and we’ll help you sort it out.
