#!/usr/bin/env python
from argparse import ArgumentParser
from distutils.util import get_platform
from setuptools import find_packages, setup

parser = ArgumentParser()
parser.add_argument("--plat-name", type=str, default=get_platform())
args, unknown_args = parser.parse_known_args()

if args.plat_name == "win32":
    source_path = "src/main/win32"
elif args.plat_name == "win-amd64":
    source_path = "src/main/win-amd64"
else:
    raise OSError("mosi-cbc does not support '%s' platform" % args.plat_name)

long_description = "!!! pypandoc and/or pandoc not found, long_description is bad, don't upload this to PyPI !!!"

if any(arg in unknown_args for arg in ["sdist", "bdist_wheel"]):
    try:
        # noinspection PyUnresolvedReferences
        from pypandoc import convert, download_pandoc

        download_pandoc()
        long_description = convert("README.md", "rst")

    except (ImportError, OSError):
        pass

setup(
    name="mosi-cbc",
    version="0.0.1",
    description="CBC solver plugin for the mosi package.",
    long_description=long_description,
    url="https://github.com/alexbahnisch/mosi-cbc",
    author="Alex Bahnisch",
    author_email="alexbahnisch@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5"
        "Programming Language :: Python :: 3.6"
    ],
    keywords="mosi cbc",
    packages=find_packages(source_path),
    package_dir={"": source_path},
    package_data={"": ["cbc.exe"]},
    install_requires=[
        "mosi>=0.0.3"
    ],
    setup_requires=[
        "pypandoc>=1.4"
    ],
    tests_require=[
        "pytest>=3.2.3",
        "pytest-runner>=2.12.1"
    ],
    test_suite="src.tests"
)
