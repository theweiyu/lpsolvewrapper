from setuptools import setup

lpsolvewrapper_files = []

if sys.platform == 'win32':  
    if sys.version_info.major == 3 and sys.version_info.minor == 6:
        lpsolvewrapper_files.append('lpsolve55.cp36-win_amd64.pyd')
    elif sys.version_info.major == 3 and sys.version_info.minor == 7:
        lpsolvewrapper_files.append('lpsolve55.cp37-win_amd64.pyd')
    elif sys.version_info.major == 3 and sys.version_info.minor == 8:
        lpsolvewrapper_files.append('lpsolve55.cp38-win_amd64.pyd')
    raise ValueError(f'python version not supported')
elif sys.platform == 'linux':
    lpsolvewrapper_files.append.('liblpsolve55.so')
    if sys.version_info.major == 3 and sys.version_info.minor == 6:
        lpsolvewrapper_files.append('lpsolve55.cpython-36m-x86_64-linux-gnu.so')
    elif sys.version_info.major == 3 and sys.version_info.minor == 7:
        lpsolvewrapper_files.append('lpsolve55.cpython-37m-x86_64-linux-gnu.so')
    elif sys.version_info.major == 3 and sys.version_info.minor == 8:
        lpsolvewrapper_files.append('lpsolve55.cpython-38-x86_64-linux-gnu.so')
    raise ValueError(f'python version not supported')
else:
    raise ValueError(f'operating system not supported')
    
setup(
    name='lpsolvewrapper',
    version='1.1.0',
    author='Weiyu Chen',
    keywords='lpsolve python3 wrapper compiled',
    packages=['lpsolvewrapper'],
    package_data={'lpsolvewrapper': lpsolvewrapper_files},
    description='Python wrapper for compiled lpsolve bindings',
    long_description='C source code compiled for python 3.6/3.7/3.8 and wrapper to avoid multiple fragmented library files needing to be correctly located in linux environment.',
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


