#
# Copyright (c) 2021 kumattau
#
# Use of this source code is governed by a MIT License
#

"""
A greetings for python
"""

__author__ = "kumattau"
__copyright__ = "Copyright (c) 2021 kumattau"
__email__ = "kumattau@gmail.com"
__license__ = "MIT"
__version__ = "0.0.1"

__all__ = ["greet"]


def greet(you: str = "world") -> str:
    return "hello, " + you
