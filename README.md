T411 API
===================

[![PyPi](https://img.shields.io/pypi/v/t411api.svg)](https://pypi.python.org/pypi/t411api)
[![Travis-CI](https://api.travis-ci.org/Xide/t411api.svg)](https://travis-ci.org/Xide/t411api)


----------
Installation
-------------

### Via pip

```sh
# stable version
pip3 install t411api
# upstream version
pip3 install git+https://git@github.com/Xide/t411api
```

### The basic way

```sh
git clone git@github.com:Xide/t411api.git && cd t411api
pip3 install -r requirements.txt
python3 ./setup.py install
```
Use this method if you want the latest (maybe less stable) updates.


> Note: The code is not yet compatible with python2

----------
FAQ
-------------

Getting a ```ServiceError```:
> This error is usually used when T411 is unreachable or encounter an unknown problem, check for [API status](http://www.websitedown.info/api.t411.in)
> If this service is up, please contact a project developer

Getting an import error:
> Some dependencies may have changed, try to run **pip install -r requirements.txt** to refresh dependency list

----------
Developers
-------------

Hi, wanna join us ? Glad to hear that !
You can start browse the code, we are trying to comment a lot, especially for TODO's.
Or you can try to improve one of theses :

	- Test coverage
	- Windows compatibility


