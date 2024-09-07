
from time import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{str(args)[0:10]} {kwargs} Took {total_time * 1000:.8f} milliseconds')
        # print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.8f} seconds')
        return result
    return timeit_wrapper

