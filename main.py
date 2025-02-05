from fastapi import FastAPI
from props import error_reponse, is_prime, is_perfect, is_armstrong, is_even_or_odd, digit_sum, fun_fact

app = FastAPI()

@app.get("/api/classify-number/{number}")
async def get(number):
    if "." in number:
        return error_reponse
    try:
        number = int(number)
    except:
        return error_reponse
    
    response_dict = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": (["armstrong"] if is_armstrong(number) else []) + [is_even_or_odd(number)],
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact(number)
    }

    return response_dict
