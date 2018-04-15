"""create a function to return n-th fibonacci number
"""

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def dynamic_fib(n):
    """dynamic programming implementation of fib()
    """
    raise NotImplementedError
