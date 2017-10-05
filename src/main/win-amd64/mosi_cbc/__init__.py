from os.path import dirname, join, realpath

"""
Package containing win-amd64 cbc (version: 2.9.9) executable.
"""

__version__ = "0.0.1"


def get_cbc_path():
    return join(dirname(realpath(__file__)), "cbc.exe")
