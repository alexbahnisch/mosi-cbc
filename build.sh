#!/bin/bash
python setup.py bdist_wheel --plat-name win32
rm -rf build
python setup.py bdist_wheel --plat-name win-amd64
rm -rf build
