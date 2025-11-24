from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"Response":"Hello World!"}
