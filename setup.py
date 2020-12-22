#! /usr/bin/env python
# coding=utf-8
import codecs
from distutils.core import setup

import os
from setuptools import find_packages


def get_readme():
    return codecs.open("README.rst", encoding="utf-8").read()


setup(
    name="pyldraw",
    description="A package for working with LDraw format files.",
    long_description=get_readme(),
    author=" David Boddie <david@boddie.org.uk>",
    maintainer="Matthieu Berthomé <rienafairefr@gmail.com>",
    author_email="rienairefr@gmail.com, david@boddie.org.uk",
    # MDW: Hacking this to work with my local setup.
    #version=os.environ.get("TAG_NAME", os.environ.get("TRAVIS_TAG", "dev")),
    version="0.8.3",
    python_requires=">=3.5, <3.9",
    packages=find_packages(),
    package_data={"ldraw": ["templates/*.mustache"]},
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    entry_points={
        "console_scripts": [
            "ldr2inv = ldraw.tools.ldr2inv:main",
            "ldr2png = ldraw.tools.ldr2png:main",
            "ldr2pov = ldraw.tools.ldr2pov:main",
            "ldr2svg = ldraw.tools.ldr2svg:main",
        ],
    },
    install_requires=[
        "appdirs",
        "numpy",
        "pymklist",
        "pystache",
        "attrdict",
        "progress",
        "PyYaml",
        "Pillow",
    ],
)
