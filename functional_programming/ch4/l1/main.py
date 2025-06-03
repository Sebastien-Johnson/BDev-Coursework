def factorial_r(x):
    if x-1 == 0 or x*x == 0:
        return max(x, 1)

    return x*(factorial_r(x-1))