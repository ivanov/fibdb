
def fib(n):
    if n < 0:
        raise ValueError("Fibonacci only defined for natural numbers")
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
