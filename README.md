f2pydemo
========

A demonstration of my annoyance with / ignorance of setuptools + f2py.

First do:
```
python setup.py build_ext -i
```
which should produce an error.

Then check where the compiled library ends up going:
```
find . -iname '*mod2*'
```
