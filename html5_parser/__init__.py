#!/usr/bin/env python
# vim:fileencoding=utf-8
# License: Apache 2.0 Copyright: 2017, Kovid Goyal <kovid at kovidgoyal.net>

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from collections import namedtuple

from .html_parser import MAJOR, MINOR, VERSION, parse

parse
version = namedtuple('Version', 'major minor patch')(MAJOR, MINOR, VERSION)
