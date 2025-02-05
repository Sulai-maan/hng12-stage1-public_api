from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/api/classify-number/{number}")
async def get(number):
    #do some edge checking
    fun_fact = requests.get(f"http://numbersapi.com/{number}/math").text
