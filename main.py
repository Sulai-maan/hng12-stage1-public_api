from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/api/classify-number/{number}")
async def get(number):
    #do some edge checking
    if any(n != )
    try:
        number = int(number)
    if isinstance(number, int):
        fun_fact = requests.get(f"http://numbersapi.com/{number}/math").text
    else:
        response = {
            "number": "alphabet",
            ""
                    }
        return 
