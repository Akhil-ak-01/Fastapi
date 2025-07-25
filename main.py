from typing import Union

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# ...existing code...

L = {
    "1":"APPLE",
    "2":"BANANA",
    "3":"CHERRY",
    "4":"DATE"
}
@app.get("/get_list/")
def read_root():
    return L
@app.post("/post_list/")
def read_root():
    return {"Hello":"AK"}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}