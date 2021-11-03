#
# Copyright (c) 2021 kumattau
#
# Use of this source code is governed by a MIT License
#

"""
A helloworld module
"""

__version__ = "0.0.1"

__all__ = ["say_helloworld"]


def say_helloworld() -> str:
    return "hello, world"
