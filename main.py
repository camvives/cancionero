from fastapi import FastAPI

app = FastAPI()  # <--- Esta es la línea que busca Uvicorn

@app.get("/")
def home():
    return {"mensaje": "¡Hola Mundo!"}