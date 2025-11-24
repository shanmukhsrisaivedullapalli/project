from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"Response":"Hello World!"}

@app.get("/{name}")
def get_name(name: str):
    return {"Response":{"Name":name}}
