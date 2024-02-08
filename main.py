from fastapi import FastAPI
import shortuuid

app = FastAPI()

items = {}

@app.put("/createurl/{url}")
def create_url(url: str):
    uuid=shortuuid.uuid()
    items[uuid] = url
    return {"uuid": uuid, "targetURL": items[uuid]}

@app.get("/geturl/{uuid}")
def get_url(uuid: str):
    return {"uuid": uuid, "targetURL": items[uuid]}

@app.get("/readdictionary/")
def read_dictionary():
    return items