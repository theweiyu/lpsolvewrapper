# lpsolvewrapper
Python3.6 wrapper for compiled lpsolve bindings

C source code compiled for python 3.6 (64-bit) and wrapper to avoid multiple fragmented library files needing to be correctly located in linux environment. This is has been tested on Ubuntu and Windows 7/10. See official [lpsolve website](http://lpsolve.sourceforge.net/5.5/) for more information.

## Installation

`pip install lpsolvewrapper`

**Install from Git:**
`pip install git+https://github.com/theweiyu/lpsolvewrapper`

**Install from Wheel:**
`pip install lpsolvewrapper-1.0.0-py3-none-any.whl`

## Usage
`from lpsolvewrapper import lp_solve`

## Compile from source (linux)
1. (Optional) First set up a python venv: `python3.6 -m venv venv1`. And activate this.
2. First build the liblpsolve55.so binary: `sh src/lpsolve55/ccc`. This is dynamically loaded by the lpsolve driver (lpsolve55.so) as a dependency
3. Update src/extra/Python/setup.py so that `LPSOLVE55=` points to the build directory containing liblpsolve55.so
4. To compile the driver: `python src/extra/Python/setup.py install`

## Troubleshooting
`ModuleNotFoundError: No module named 'lpsolve55'` Make sure you are using Python 3.6 64-bit. If you continue to have this issue, check that the lpsolve55 binaries are successfully copied into site-packages upon import lpsolvewrapper for the first time. If you want to use a different version of python you'll need to re-compile from source (see above).
