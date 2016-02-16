# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals


def stripQuotes(s, loc, toks):
    """Strip the actual quotes from the tokens in `toks`.

    Note: This is because it turned out `QuotedString` was stripping
    first and last characters of a matched string regardless. If
    there's a way to avoid having this function - by all means it
    should be removed.

    """
    return [t.strip("'") for t in toks]
