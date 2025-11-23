import random

def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None):
    if seed is not None:
        random.seed(seed)

    if distinct:
        if hi - lo + 1 < n:
            raise ValueError("Невозможно сгенерировать.")
        return random.sample(range(lo, hi + 1), n)
    else:
        return [random.randint(lo, hi) for _ in range(n)]

def nearly_sorted(n: int, swaps: int, *, seed=None):
    if seed is not None:
        random.seed(seed)

    arr = list(range(n))
    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def many_duplicates(n: int, k_unique=5, *, seed=None):
    if seed is not None:
        random.seed(seed)

    unique_values = rand_int_array(k_unique, 0, 100, distinct=True, seed=seed)
    return [random.choice(unique_values) for _ in range(n)]

def reverse_sorted(n: int):
    return list(range(n - 1, -1, -1))

def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None):
    if seed is not None:
        random.seed(seed)

    return [random.uniform(lo, hi) for _ in range(n)]
