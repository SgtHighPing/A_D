from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib())