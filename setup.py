#   # ------------------------------------------------------------------ #
#   |  ░▀▀█░█▀▀░█▀▀░█▀▀░█▀█░█▄█░█▄█░█▀█░█▀█░█░░░▀█▀░█▀▄░█▀▄░█▀█░█▀▄░█░█  |
#   |  ░▄▀░░█░░░▀▀█░█░░░█░█░█░█░█░█░█░█░█░█░█░░░░█░░█▀▄░█▀▄░█▀█░█▀▄░░█░  |
#   |  ░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀░░▀░▀░▀░▀░▀░▀░░▀░  |
#   #------------------------------------------------------------------- #
#   Website: https://commonlib.zandercraft.ca
#   Documentation: https://github.com/Zandercraft/ZCSCommonLibrary/wiki/
#   License: Mozilla Public License 2.0
#   # -------------------------------------------------------------------------------- #
#   * Main setup.py file for zcscommonlib. Defines all attributes of the library.      *
#   # -------------------------------------------------------------------------------- #

# Imports
from setuptools import find_packages, setup
import pypandoc

# Convert README.md file to proper format for PyPi description (long_description)
try:
    description = pypandoc.convert_file('README.md', 'rst', 'str')
except (IOError, ImportError):
    description = open('README.md').read()

# Define all project properties
setup(
    name='zcscommonlib',
    packages=find_packages(include=['zcscommonlib']),
    # TODO: Make sure to increment this with every version bump
    version='0.3.4',
    description='A Common Library For Use In Computer Science Projects',
    # Set the long description to the README.md file contents
    long_description=description,
    long_description_content_type="text/markdown",
    author='Zandercraft',
    # Homepage of the Library
    url='https://commonlib.zandercraft.ca',
    # TODO: Always make sure to update the download url with every version bump
    download_url='https://github.com/Zandercraft/ZCSCommonLibrary/archive/0.3.4.tar.gz',
    # License: Mozilla Public License 2.0
    license='MPL 2.0',
    # Library dependencies
    install_requires=[],
    # Packages required for building library
    setup_requires=['pytest-runner', 'pypandoc'],
    # Packages required for running tests
    tests_require=['pytest==6.2.2'],
    test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',  # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Python versions to support
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
