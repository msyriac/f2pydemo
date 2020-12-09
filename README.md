f2pydemo
========

A demonstration of my annoyance with setuptools + f2py.

First do:
```
python setup.py build_ext -i
```
which should produce an error.

Then see where the compiled library is using:
```
find . -iname '*mod2*'
```