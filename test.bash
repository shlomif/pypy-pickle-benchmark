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
args="e657.py 2 2000"
time python3 $args
time pypy3 $args
time pypy3 $args
