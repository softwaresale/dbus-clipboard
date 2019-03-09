#!/usr/bin/env python3
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dbus-clipboard",
    version="0.0.1",
    author="Charlie Sale",
    author_email="softwaresale01@gmail.com",
    description="A dbus-based clipboard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/softwaresale/dbus-clipboard",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points = {
        'console_scripts': [
            'dbus-clipboard=dbuscb.main:main'
        ],
    },
)
