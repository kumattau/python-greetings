#
# Copyright (c) 2021 kumattau
#
# Use of this source code is governed by a MIT License
#

import hello


def test_hello():
    assert hello.say_hello() == "hello, world"
