from os import path
from setuptools import setup, find_packages


setup(
    name='Word4Univer',
    version='0.1.0',
    package_dir={'': path.dirname(__file__)},
    packages=find_packages(path.dirname(__file__), exclude=["tests*"]),
    url='',
    license='MIT',
    author='chiririll',
    author_email='sstive39@gmail.com',
    description='',
    requires=['Jinja2']
)
