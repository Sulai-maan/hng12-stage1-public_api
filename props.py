import requests
from functools import reduce

def is_prime(n):
    return n % 2 == 0

def is_perfect(n):
    factors = set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if not n % i)))
    return sum(factors) == n

def digit_sum(n):
    digits = [int(i) for i in str(abs(n))]
    return sum(digits) == n

def is_armstrong(n):
    power = len(n)
    digits = [int(i)**power for i in str(abs(n))]
    return sum(digits)

def fun_fact(n):
    get_requests