# lpsolvewrapper
Python wrapper for compiled lpsolve bindings. Compatible with Python 3.6, 3.7, 3.8 on Linux (glibc) and Windows 64bit

Compiled lpsolve C source code and wrapper to avoid multiple fragmented library files needing to be correctly located in linux environment. This has been tested on Ubuntu and Windows 7/10. See official [lpsolve website](http://lpsolve.sourceforge.net/5.5/) for more information.

## Installation

`pip install lpsolvewrapper`

**Install from Git:**
`pip install git+https://github.com/theweiyu/lpsolvewrapper`


## Usage
`from lpsolvewrapper import lp_solve`

## Compile from source (linux)
1. (Optional) First set up a python venv: `python -m venv venv1`. And activate this.
2. First build the liblpsolve55.so binary: `sh src/lpsolve55/ccc`. This is dynamically loaded by the lpsolve driver (lpsolve55.so) as a dependency
3. Update src/extra/Python/setup.py so that `LPSOLVE55=` points to the build directory containing liblpsolve55.so
4. To compile the driver: `python src/extra/Python/setup.py install`

## Troubleshooting
`ModuleNotFoundError: No module named 'lpsolve55'` Make sure you are using a compatible version of python 64-bit. If you continue to have this issue, check that the lpsolve55 binaries are successfully copied into site-packages upon importing lpsolvewrapper for the first time. If you want to use a different version of python you'll need to re-compile from source (see above).
