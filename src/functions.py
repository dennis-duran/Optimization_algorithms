import math

def rosenbrock(x):
    sum = 0
    for i in range(0, 1):
        sum += 100 * (x[i + 1] - x[i] * x[i]) ** 2 + (x[i] - 1) ** 2
    return sum


def salomon(x):
    sum = 0
    for i in range(0, 2):
        sum += x[i] ** 2

    return 1 - math.cos(2 * math.pi * math.sqrt(sum)) + 0.1 * math.sqrt(sum)
