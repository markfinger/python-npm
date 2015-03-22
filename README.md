python-npm
==========

[![Build Status](https://travis-ci.org/markfinger/python-npm.svg?branch=master)](https://travis-ci.org/markfinger/python-npm)

Python bindings and utils for [npm](http://npmjs.com).

```python
from npm.bindings import npm_install

# Install the dependencies in a directory containing a package.json
npm_install('/path/to/some/directory/')
```

Installation
------------

`pip install npm`

Bindings
--------

### npm.bindings.npm_install()

Invokes npm's install command in a specified directory. `install` blocks the python
process and will direct npm's output to stdout.

A typical use case for `install` is to ensure that your dependencies specified in
a `package.json` file are installed during runtime. The first time that `install` is 
run in a directory, it will block until the dependencies are installed to the file
system, successive calls will resolve almost immediately. Installing your dependencies 
at run time allows for projects and apps to easily maintain independent dependencies 
which are resolved on demand.

Arguments:

- `target_dir`: a string pointing to the directory which the command will be invoked in.

```python
import os
from npm.bindings import npm_install

# Install the dependencies in a particular directory's package.json
npm_install('/path/to/some/directory/')

# Install the dependencies in the same directory as the current python file
npm_install(os.path.dirname(__file__))
```

### npm.bindings.npm_run()

Invokes npm with the arguments provided and returns the resulting stderr and stdout.

```python
from npm.bindings import npm_run

stderr, stdout = npm_run('install', '--save', 'some-package')
```

### npm.bindings.ensure_npm_installed()

Raises an exception if npm is not installed.

### npm.bindings.ensure_npm_version_gte()

Raises an exception if the installed version of npm is less than the version required.

Arguments:

- `version_required`: a tuple containing the minimum version required.

```python
from npm.bindings import ensure_npm_version_gte

ensure_npm_version_gte((2, 0, 0,))
```

### npm.bindings.is_installed

A boolean indicating if npm is installed.

### npm.bindings.version

A tuple containing the version of npm installed. For example, `(2, 0, 0)`

### npm.bindings.version_raw

A string containing the raw version returned from npm. For example, `'2.0.0'`



Running the tests
-----------------

```bash
mkvirtualenv python-npm
pip install -r requirements.txt
nosetests
```
