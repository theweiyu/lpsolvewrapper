from setuptools import setup

setup(
    name='lpsolvewrapper',
    version='1.0.0',
    author='Weiyu Chen',
    packages=['lpsolvewrapper'],
    package_data={'lpsolvewrapper': ['lpsolve55.cp36-win_amd64.pyd', 'liblpsolve55.so', 'lpsolve55.cpython-36m-x86_64-linux-gnu.so', 'lpsolve55-5.5.0.9-py3.6.egg-info']}
)

