from functools import wraps
from time import time

def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Total execution time for {func.__name__} : {end_ if end_ > 0 else 0} ms")
    return _time_it


def enforce_float_type(num: [float, int, str]) -> float:
    return float("{:.10f}".format(num))