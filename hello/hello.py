#
# Copyright (c) 2021 kumattau
#
# Use of this source code is governed by a MIT License
#

"""
A hello package
"""

__version__ = "0.0.1"

__all__ = ["say_hello"]


def say_hello(you: str = "world") -> str:
    return "hello, " + you
