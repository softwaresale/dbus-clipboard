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
        "License :: OSI Approved :: GPLv3+",
        "Operating System :: OS Independent",
    ],
)