from functools import wraps

def memoize(func):
    wraps(func)
    def wrapper(self):
        if not hasattr(self, "__memoize_cache"):
            self.__memoize_cache = {}
        if func.func_name not in self.__memoize_cache:
            self.__memoize_cache[func.func_name] = func(self)
        return self.__memoize_cache[func.func_name]
    return wrapper
