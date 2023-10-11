from setuptools import setup

setup( 
    name='whyslow', 
    version='0.0.2', 
    description='Developer-friendly performance profiling utilities for Python', 
    author='valentinstn', 
    packages=['whyslow'], 
    python_requires='>=3.6',
    install_requires=[ 
        'snakeviz'
    ], 
) 
