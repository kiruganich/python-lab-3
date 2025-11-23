def factorial(n):
    if n < 0:
        raise ValueError("Не определено для отрицательных чисел")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_rec(n):
    if n < 0:
        raise ValueError("Не определено для отрицательных чисел")
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)


def fib(n):
    if n < 0:
        raise ValueError("Не определено для отрицательных индексов")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fib_rec(n):
    if n < 0:
        raise ValueError("Не определено для отрицательных индексов")
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)
