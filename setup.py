from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

setup(
    # Application name:
    name="thesis",

    # Version number (initial):
    version="0.0.0",

    # Application author details:
    author="Vanessa Sochat",
    author_email="vsochat@stanford.edu",

    # Packages
    packages=find_packages(),

    # Data files
    include_package_data=True,
    zip_safe=False,

    # Details
    url="http://www.github.com/vsoch/thesis",

    license="LICENSE",
    description="Convert Stanford LaTeX Thesis into Web Version for Github Pages",
    keywords='thesis, book, website, Stanford',

    install_requires = ['numpy','Flask','gitpython'],

    entry_points = {
        'console_scripts': [
            'thesis=thesis.scripts:main',
        ],
    },

)
