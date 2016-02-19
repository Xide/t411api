	T411 API
===================

[![PyPi](https://img.shields.io/pypi/v/t411api.svg)](https://pypi.python.org/pypi/t411api)
[![Travis-CI](https://travis-ci.org/Xide/t411api.svg)](https://travis-ci.org/Xide/t411api)


----------
Installation
-------------

### Compatibility

> This code is developped with Python 3.5
> However, it sould be compatible Python >= 3.3, but remains untested.

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
python3 ./setup.py install
```

Use this method if you want the latest (maybe less stable) updates.

----------
Usage
-------------
The API is exposed with the ```T411API``` class.

API functions ( excepted ```connect``` will return a dictionnary containing the JSON datas returned by the API ( or raise upon unrecoverable error ) 

#### Connection

The T411 api only support plain-text authentication, the ```connect``` method will allow you to retreive your token ( mandatory to use the API ).

```python
>>> import t411api
>>> api = t411api.T411API()
>>> api.connect('username', 'password')
```

The API will raise a ```ServiceError``` or ```ConnectionError``` upon failure, details of the errors can be extracted from exception string.

Otherwise, the ```api.token``` and ```api.uid``` fields will be set to the corresponding values.

#### Search

the ```T411api.search``` function provide search functionnality.

```python3
>>> # T411API.search(query, **kwargs)
>>> # Query is the mandatory string for your search
>>> # kwargs are the T411 optionals arguments (ie: 'limit'
>>> # argument that will fix the maximum number of responses )
>>> api.search('archlinux', limit=10)

```

#### Retrieving Top lists

To fetch T411 tops, you can use the ```T411API.top``` method.
The only parameter of the method is a string containing the name of the top you need.
For more details about the API parameters, you can visit http://api.t411.in/.
At the time we are writting this documentation, choices are :

-  100
- day
- week
- month

```python
>>> api.top('100')
```

#### Torrent details

The ```T411API.details``` method retrieve details about a torrent 
```python
>>> # Retrieve details for the first 'archlinux' torrent
>>> id = api.search('archlinux')['torrents'][0]['id']
>>> details = api.details(int(id))
```

#### Downloading torrents

The ```T411API.download``` handle torrent downloading. 
She receive up to 3 parameters:

1.  torrent_id : mandatory, the ID of the torrent you want to download
2. filename : optionnal, the name of the downloaded torrent file ( torrent name by default )
3. base: optional: directory where the torrent file will be created ( current directory by default )

```python
>>> # Download the first 'archlinux' torrent
>>> id = api.search('archlinux')['torrents'][0]['id']
>>> path = api.download(int(id))
```

#### User informations
```T411API.user``` method return informations about an user.

#### Bookmarks

The bookmarks management is provided by 3 methods: 

1. ```T411API.bookmarks```
		This method return the current user bookmarks
2.  ```T411API.add_bookmark```
3.  ```T411API.del_bookmark```

----------
Exceptions
-------------
Classes:
```
  builtins.Exception(builtins.BaseException)
        APIError
            ConnectError
            ServiceError
```

**``` class APIError(builtins.Exception)```**
     >  Exception thrown upon an unknow API error
     >  Base class for every API exceptions

**```class ConnectError(APIError)```**
     > Exception thrown when an error occur
     >  on client side ( most likely receivable error )

**```class ServiceError(APIError)```**
    >  Exception thrown when T411 service encounter an error

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

