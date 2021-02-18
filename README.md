# ZCSCommonLibrary

![GitHub top language](https://img.shields.io/github/languages/top/Zandercraft/ZCSCommonLibrary) <a href="https://pypi.org/project/zcscommonlib/"> ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zcscommonlib) </a> ![Python package](https://github.com/Zandercraft/ZCSCommonLibrary/workflows/Python%20package/badge.svg) ![CodeQL](https://github.com/Zandercraft/ZCSCommonLibrary/workflows/CodeQL/badge.svg) <a href = "https://pypi.org/project/zcscommonlib/"> ![PyPi Package Deployment](https://github.com/Zandercraft/ZCSCommonLibrary/workflows/Upload%20Python%20Package/badge.svg) </a> <a href="https://commonlib.zandercraft.ca"> ![Website](https://img.shields.io/website?down_message=offline&label=Website&up_message=online&url=https%3A%2F%2Fcommonlib.zandercraft.ca) </a>

A Common Library For Use In Computer Science Projects

**PIP Package**: zcscommonlib <br />
**Current Version:** <a href = "https://pypi.org/project/zcscommonlib/"> ![PyPI](https://img.shields.io/pypi/v/zcscommonlib) </a> <br />
**License**: Mozilla Public License Version 2.0

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) [![Contribution Guide](https://img.shields.io/badge/Contributions%20Guide-Click%20Here!-limegreen.svg)](CONTRIBUTING.md)

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
