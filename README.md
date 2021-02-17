# ZCSCommonLibrary

![GitHub top language](https://img.shields.io/github/languages/top/Zandercraft/ZCSCommonLibrary) ![Python package](https://github.com/Zandercraft/ZCSCommonLibrary/workflows/Python%20package/badge.svg) ![CodeQL](https://github.com/Zandercraft/ZCSCommonLibrary/workflows/CodeQL/badge.svg) ![PyPi Package Deployment](https://github.com/Zandercraft/ZCSCommonLibrary/workflows/Upload%20Python%20Package/badge.svg)

A Common Library For Use In Computer Science Projects

**PIP Package**: zcscommonlib <br />
**Current Version:** https://img.shields.io/github/v/release/Zandercraft/ZCSCommonLibrary?include_prereleases <br />
**License**: Mozilla Public License Version 2.0

### Importing The Library
```python
from zcscommonlib import functions as zcs
# Then use the functions as zcs.function()
```

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

### Wiki/Documentation
All documentation for ZCSCommonLibrary is available [here](https://github.com/Zandercraft/ZCSCommonLibrary/wiki).
