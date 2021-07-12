from setuptools import setup

setup(
    name='lpsolvewrapper',
    version='1.0.1',
    author='Weiyu Chen',
    keywords='lpsolve python3 wrapper compiled',
    packages=['lpsolvewrapper'],
    package_data={'lpsolvewrapper': ['lpsolve55.cp36-win_amd64.pyd', 'liblpsolve55.so', 'lpsolve55.cpython-36m-x86_64-linux-gnu.so', 'lpsolve55-5.5.0.9-py3.6.egg-info']},
    description='Python3.6 wrapper for compiled lpsolve bindings',
    long_description='C source code compiled for python 3.6 and wrapper to avoid multiple fragmented library files needing to be correctly located in linux environment.',
    long_description_content_type='text/plain',
    url='https://github.com/theweiyu/lpsolvewrapper',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3.6'
    ],
    zip_safe = False,
)


