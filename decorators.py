from collections.abc import Iterable 
from typing import TypeVar
import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args,**kwargs):
        time_start = time.perf_counter()
        result = func(*args,**kwargs)
        elapsed = time.perf_counter() - time_start 
        args_str=','.join(repr(arg) for arg in args)
        print(f"[{elapsed:0.8}s] {func.__name__}({args_str}) -> ({result})")
        return result
    return clocked   
@functools.cache
@clock
def fibonacci(n): 
    if n < 2: return n
    return fibonacci(n - 2) + fibonacci(n - 1)

if __name__=='__main__':
    fibonacci(87)
