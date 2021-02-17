from setuptools import find_packages, setup

setup(
    name='zcscommonlib',
    packages=find_packages(include=['zcscommonlib']),
    version='0.3.0',
    description='A Common Library For Use In Computer Science Projects',
    author='Zandercraft',
    url='https://github.com/Zandercraft/ZCSCommonLibrary',
    download_url='https://github.com/Zandercraft/ZCSCommonLibrary/archive/0.2.0.tar.gz',
    license='MPL 2.0',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.2'],
    test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',  # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
