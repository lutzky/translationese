"""Usable as a wrapper to a method, caches execution results.

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
    try:
        if os.path.exists(filename):
            with open(filename, "r") as f:
                obj._memoize_cache = pickle.load(f)
    except Exception:
        logging.warn("Invalid pickle file %s", filename)

def dump(obj, filename):
    if hasattr(obj, "_memoize_cache"):
        with open(filename, "w") as f:
            pickle.dump(obj._memoize_cache, f)
