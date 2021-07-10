# lpsolvewrapper
Python3.6 wrapper for compiled lpsolve bindings

C source code compiled for python 3.6 (64-bit) and wrapper to avoid multiple fragmented library files needing to be correctly located in linux environment.

## Installation

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
