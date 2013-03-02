"""
This module provides the ``@memoize`` decorator, which is used as
a method decorator. Decorating a method with ``@memoize`` will cause
its result to be cached in the hidden ``_memoize_cache`` property, and subsequent calls will return this cache.

This particular implementation of memoize does not support methods with
arguments (other than the implicit ``self`` argument). However, it *does*
support :mod:`pickle` serialization.

>>> from memoize import memoize
>>> class K:
...     def __init__(self):
...         self.x = 5
...     @memoize
...     def m(self):
...         return self.x * 2
>>> k = K()
>>> k.m()
10
>>> k.x = 6
>>> k.m() # Will not recompute
10
>>> import pickle
>>> s = pickle.dumps(k) # resulting objects can be pickled!
"""

from functools import wraps
import cPickle as pickle
import os
import logging

logger = logging.getLogger("memoize")

# pylint: disable=W0212

def memoize(func):
    @wraps(func)
    def wrapper(self):
        if not hasattr(self, "_memoize_cache"):
            self._memoize_cache = {}
        if func.func_name not in self._memoize_cache:
            self._memoize_cache[func.func_name] = func(self)
        return self._memoize_cache[func.func_name]
    return wrapper

def load(obj, filename):
    """Loads :mod:`pickle` data (saved by :func:`dump`) from ``filename``
    and injects it into ``obj``'s cache."""
    try:
        if os.path.exists(filename):
            with open(filename, "r") as f:
                obj._memoize_cache = pickle.load(f)
    except Exception:
        logging.warn("Invalid pickle file %s", filename)

def dump(obj, filename):
    """Dumps ``obj``'s memoized cache as :mod:`pickle` data into ``filename``.
    """
    if hasattr(obj, "_memoize_cache"):
        with open(filename, "w") as f:
            pickle.dump(obj._memoize_cache, f)
