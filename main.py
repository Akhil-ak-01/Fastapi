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
def get_list():
    return L

@app.post("/post_list/")
async def post_list(request: Request):
    data = await request.json()
    key = data.get("key")
    value = data.get("value")
    if key and value:
        L[key] = value
        return {"message": "Item added!", "list": L}
    return {"error": "Missing key or value"}
    

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}