import requests
from functools import reduce

def is_even_or_odd(n: int) -> str:
   if n % 2:
      return "odd"
   else:
      return "even"
   
def is_prime(n: int) -> bool:
#    n = abs(n)
   if n == 2:
      return True
   elif n < 2 or not n % 2:
      return False
   else:
      return any((not n % i) for i in range(3, int(n**0.5) + 1, 2))

def is_perfect(n: int) -> bool:
    if n < 6:
       return False
    
    factors = set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if not n % i)))
   
    factors.discard(n)
    return sum(factors) == n

def digit_sum(n: int) -> int:
    digits = [int(i) for i in str(abs(n))]
    return sum(digits)

def is_armstrong(n: int) -> int:
    
    power = len(str(n))
    print(power)
    digits = [int(i)**power for i in str(abs(n))]
    return sum(digits) == n

def get_fun_fact(n: int) -> str:
    response = requests.get(f"http://numbersapi.com/{n}/math")
    
    if response.status_code == 200:
       return response.text
    else:
       return "bad request"
    
error_reponse = {
   "number": "alphabet",
    "error": True
}
