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


def defaultValue(value):
    """Return a default value.

    Useful when `Optional` does not match, but some value should still
    be set in `ParseResult`.

    """
    def _default(toks):
        if not toks:
            return [value]
        if len(toks) == 1 and not toks[0]:
            return [value]

    return _default
