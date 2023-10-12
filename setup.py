from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup( 
    name='whyslow', 
    version='0.1.7', 
    description='Developer-friendly performance profiling utility for Python', 
    long_description=long_description,
    long_description_content_type="text/markdown",    
    author='valentinstn', 
    packages=['whyslow'], 
    python_requires='>=3.6',
    install_requires=[ 
        'snakeviz'
    ], 
    project_urls={
        "GitHub": "https://github.com/valentinstn/whyslow",
    },
) 
