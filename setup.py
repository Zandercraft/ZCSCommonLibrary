from setuptools import find_packages, setup
setup(
    name='zcscommonlib',
    packages=find_packages(include=['zcscommonlib']),
    version='0.1.0',
    description='A Common Library For Use In Computer Science Projects',
    author='Zandercraft',
    url='https://zandercraft.ca',
    license='MPL 2.0',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.2'],
    test_suite='tests',
)
