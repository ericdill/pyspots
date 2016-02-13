[![Build Status](https://travis-ci.org/ericdill/pyspots.svg?branch=master)](https://travis-ci.org/ericdill/pyspots)

# pyspots

A work in progress to extract the useful bits of the original Java
implementation of [Ramdog] (https://github.com/themartinlab/Ramdog)
and rewrite it in Python.

## Installation

If you do not have Python installed on your computer, please install python 3.5
with [Anaconda] (https://www.continuum.io/downloads).  If you have the choice,
please please please do not install python 2.

After you have installed Python, I would suggest installing pyspots with the
following command:

```
pip install pyspots
```

If the above command does not work, you will need to clone the git repository
from github and install manually. Do this:

```
git clone https://github.com/themartinlab/pyspots
cd pyspots
python setup.py install
```

Then make sure it was installed
```
cd
python -c "import pyspots; print(pyramdog.__version__)"
```

If the above prints out a version number like "v0.0.1" then you have
successfully installed pyspots.  If you get an exception, please contact me
via github [here] (https://github.com/themartinlab/pyspots/issues).


## Usage

`pyspots` is meant to be used on the output files from the spotpicking
algorithms in to the Java implementation of [Ramdog]
(https://github.com/themartinlab/ramdog).

- Automatic fitting of individual spotpicking output data


## Setting up for Development

```
git clone https://github.com/themartinlab/pyspots
cd pyspots
python setup.py develop
```

And then run the test suite with `py.test` to make sure that it was
installed correctly.
