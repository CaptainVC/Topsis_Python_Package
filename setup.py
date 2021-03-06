import os
from setuptools import setup

NAME = "Topsis-Vyom-101917060"
VERSION = "1.0.1"
DESCRIPTION = "A package for topsis score generation in mere moments"
AUTHOR = "Vyom Chopra"
AUTHOR_EMAIL = "vchops652000@gmail.com"
PACKAGES_PRESENT = ['Topsis-Vyom-101917060']
PACKAGES_NEED = ['pandas','numpy']

def read_text_file(name):
    path = os.getcwd()
    return open(f"{path}\{name}.txt").read()

setup(
    name = NAME,
    version = VERSION,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    description = DESCRIPTION,
    packages = PACKAGES_PRESENT,
    install_requires = PACKAGES_NEED,
    long_description=read_text_file('README'),
    long_description_content_type='text/markdown'
)

