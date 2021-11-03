#
# Copyright (c) 2021 kumattau
#
# Use of this source code is governed by a MIT License
#

"""
A greetings for python
"""

__version__ = "0.0.1"

__all__ = ["greet"]


def greet(you: str = "world") -> str:
    return "hello, " + you
