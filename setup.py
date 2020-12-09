#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import setuptools
from distutils.errors import DistutilsError
from numpy.distutils.core import setup, Extension
import os, sys
import numpy as np

setup(
    description="f2pydemo",
    package_dir={"f2pydemo": "f2pydemo"},
    entry_points={
    },
    ext_modules=[
        Extension('f2pydemo.mod1',
                  sources=['fortran/mod1.f90'],
                  libraries = [('mod2', dict(sources=['fortran/mod2.f90']))]),
    ],
    include_package_data=True,    
    name='f2pydemo',
    zip_safe=False,
)

print('\n[setup.py request was successful.]')

