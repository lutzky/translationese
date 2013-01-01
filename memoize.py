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

def memoize(func):
    @wraps(func)
    def wrapper(self):
        if not hasattr(self, "__memoize_cache"):
            self.__memoize_cache = {}
        if func.func_name not in self.__memoize_cache:
            self.__memoize_cache[func.func_name] = func(self)
        return self.__memoize_cache[func.func_name]
    return wrapper
