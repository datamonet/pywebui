"""Setup script for webuipy"""

import os.path
from setuptools import setup

# file directory
HERE = os.path.abspath(os.path.dirname(__file__))

# README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# setup everything
setup(
    name="webuipy",
    version="0.0.1",
    description="Python API Client for A1111 WebUI",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/datamonet",
    author="DataMonet LLC",
    author_email="support@replicable.art",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["webuipy"],
    include_package_data=True,
    install_requires=[
        "importlib_resources",
    ],
    entry_points={"console_scripts": ["webuipy=webuipy.__main__:main"]},

)
