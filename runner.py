from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

# Endpoint for GPT Action — matches hello_world.json schema
@app.post("/hello")
async def say_hello():
    return JSONResponse(content={"message": "Hello World"})

# Endpoint to serve the OpenAPI schema (optional, for debugging or inspection)
@app.get("/schema")
async def get_schema():
    schema_path = os.path.join(os.path.dirname(__file__), "hello_world.json")
    with open(schema_path, "r") as f:
        schema = json.load(f)
    return schema

# For local testing only: simulate a ChatGPT POST to /hello
if __name__ == "__main__":
    import requests
    import time

    url = "http://127.0.0.1:8000/hello"
    print("Attempting test POST request to /hello...")

    # Give the server a moment if running side-by-side
    time.sleep(1)

    try:
        response = requests.post(url)
        if response.ok:
            print("Success:", response.json())
        else:
            print("Failed:", response.status_code, response.text)
    except Exception as e:
        print("Error connecting to server:", str(e))
