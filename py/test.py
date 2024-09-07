# decorator to check the speed of a function, decorator can get parameter to edit speed precision
from time import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time * 1000:.8f} milliseconds')
        # print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.8f} seconds')
        return result
    return timeit_wrapper


@timeit
def fun(a):
    n = len(a)
    for i in range(1, n):
        x = i
        k = i-1
        while a[k]>a[x] and k != -1:
            a[k], a[x] = a[x], a[k]
            k-=1
            x-=1

    print(a)

@timeit
def fun1(a):
    n = len(a)
    for i in range(1, n):
        n = a[i]
        k = i-1
        while a[k] > n and k >= 0:
            a[k+1] = a[k]
            k-=1
        a[k+1]=n

    print(a)

fun1([10,30,50,40,20, 5])
fun([10,30,50,40,20, 5])


