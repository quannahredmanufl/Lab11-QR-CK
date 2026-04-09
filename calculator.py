#https://github.com/quannahredmanufl/Lab11-QR-CK.git
# Partner 1: Quannah Redman
# Partner 2: Cole Knaus



import math
def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(a)
    except ValueError as e:
        raise e

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        raise e

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    else:
        return a / b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("ValueError")
    return math.log(b, a)

def exp(a, b):
    return a ** b


