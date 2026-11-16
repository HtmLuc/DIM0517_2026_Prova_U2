from fastapi import FastAPI

app = FastAPI()

# Endpoint /hello
@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

# Endpoint /healthy
@app.get("/healthy")
def healthy():
    return {"status": "healthy"}