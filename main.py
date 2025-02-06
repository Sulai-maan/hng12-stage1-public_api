from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from props import error_reponse, is_prime, is_perfect, is_armstrong, is_even_or_odd, digit_sum, get_fun_fact

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["Get"],
    allow_headers=["*"]
)


@app.get("/api/classify-number/", status_code=400)
async def missing_number():
    error_reponse["number"] = ""
    return error_reponse


@app.get("/api/classify-number/{number}", status_code=200)
async def get(number, response: Response):
    if "." in number:
        error_reponse["number"] = number
        response.status_code = status.HTTP_400_BAD_REQUEST
        return error_reponse
    try:
        number = int(number)
    except:
        error_reponse["number"] = number
        response.status_code = status.HTTP_400_BAD_REQUEST
        return error_reponse
    
    response_dict = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": (["armstrong"] if is_armstrong(number) else []) + [is_even_or_odd(number)],
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }

    return response_dict
