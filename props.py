import requests
from functools import reduce

def is_prime(n: int) -> bool:
   n = abs(n)
   if n == 2:
      return True
   elif not n % 2:
    return False
   else:
    return any((not n % i) for i in range(3, int(n**0.5) + 1, 2))

def is_perfect(n: int) -> bool:
    factors = set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if not n % i)))
    return sum(factors) == n

def digit_sum(n: int) -> bool:
    digits = [int(i) for i in str(abs(n))]
    return sum(digits) == n

def is_armstrong(n: int) -> int:
    power = len(n)
    digits = [int(i)**power for i in str(abs(n))]
    return sum(digits)

def fun_fact(n: int) -> str:
    response = requests.get(f"http://numbersapi.com/{n}/math")
    
    if response.status_code == 200:
       return response.text
    else:
       return "bad request"