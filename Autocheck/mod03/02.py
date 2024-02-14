def factorial(n):
    if n < 2:
        return 1  # Базовий випадок
    else:
        return n * factorial(n - 1)  # Рекурсивний випадок 


def number_of_groups(n, k):
    c = factorial(n) / (factorial(n - k) * factorial(k))
    return int(c)