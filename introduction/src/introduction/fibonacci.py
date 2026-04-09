from functools import lru_cache

@lru_cache(maxsize=None)
def compute_fibonacci(n):
    """Return the nth Fibonacci number.

    >>> compute_fibonacci(0)
    0
    >>> compute_fibonacci(1)
    1
    >>> compute_fibonacci(2)  # 0 + 1
    1
    >>> compute_fibonacci(3)  # 1 + 1
    2
    >>> compute_fibonacci(4)  # 1 + 2
    3
    """
    # BEGIN QUESTION 1.1
    
    if (n < 2):
        return n
    else:
        return compute_fibonacci(n - 1) + compute_fibonacci(n - 2)

    # END QUESTION 1.1
