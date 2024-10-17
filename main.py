from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/hello')
def read_hello():
    return '<p>Hello World</p>'