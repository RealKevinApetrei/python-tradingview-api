import codecs
import re
import os
import sys
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))


def find_packages():
    """adapted from IPython's setupbase.find_packages()"""

    packages = []

    for dir, subdirs, files in os.walk("tradingview"):
        package = dir.replace(os.path.sep, ".")
        
        if "__init__.py" not in files:
            # not a package
            continue

        if sys.version_info < (3, 4) and "asyncio" in package and "sdist" not in sys.argv:
            # Don't install asyncio packages on old Python
            # avoids issues with tools like compileall, pytest, etc.
            # that get confused by presence of Python 3-only sources,
            # even when they are never imported.
            continue
        
        packages.append(package)
    
    return packages


def read(*parts):
    with codecs.open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__  = ['\"]([^'\"]*)['\"]",
                                version_file, re.M)

    if version_match:
        return version_match.group(1)
    
    raise RuntimeError("Unable to find version string.")


def install_requires():
    requires = ["requests"]

    if sys.version_info > (3, 4):
        requires.extend(["websockets"])

    return requires


setup(
    name="python-tradingview-api",
    version=find_version("tradingview", "__init__.py"),
    packages=find_packages(),
    description="TradingView REST API v1 Python Implementation",
    url="https://github.com/RealKevinApetrei/python-tradingview-api",
    author="Kevin Apetrei",
    license="MIT",
    author_email="realkevinapetrei@gmail.com",
    install_requires=install_requires(),
    keywords="tradingview stocks crypto bitcoin ethereum btc eth python api cryptodev",
    classifiers=[
        "Intended Audience :: Developers",
        "License, :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6"
        "Programming Language :: Python :: 3.7"
        "Programming Language :: Python :: 3.8"
        "Programming Language :: Python :: 3.9"
        "Programming Language :: Python"
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)