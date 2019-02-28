#! /bin/bash
#
# test.bash
# Copyright (C) 2019 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under terms of the MIT license.
#

set -e -x
mkdir -p ~/tmp
pypy3 e657_cache.py
time python3 e657.py 2 1000
time pypy3 e657.py 2 1000
time pypy3 e657.py 2 1000
