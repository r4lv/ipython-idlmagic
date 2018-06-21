#!/usr/bin/env python

import io
import os
from setuptools import find_packages, setup

NAME = 'idlmagic'
REQUIRES_PYTHON = '>=3.0.0'
REQUIRED = [
    'IPython'
]
CLASSIFIERS = [
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Other',
        'Framework :: IPython',
        'Framework :: Jupyter',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Software Development :: Libraries'
]


here = os.path.abspath(os.path.dirname(__file__))

# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

about = {}
with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=about['__description__'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    python_requires=REQUIRES_PYTHON,
    url=about['__url__'],
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    include_package_data=True,
    license=about['__license__'],
    classifiers=CLASSIFIERS,
)