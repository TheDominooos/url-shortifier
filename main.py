from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import shortuuid
from pydantic import BaseModel, HttpUrl

app = FastAPI()

urlDict = {
    "uuid": "https://typer.tiangolo.com"
}

class createItem(BaseModel):
    url: HttpUrl

class Item(createItem):
    id: str

@app.post("/createurl")
def create_url(item: createItem):
    uuid=shortuuid.uuid()[:7]
    urlDict[uuid] = item.url
    return {"uuid": uuid, "targetURL": urlDict[uuid]}

@app.get("/geturl/{uuid}")
def get_url(uuid: str):
    #return {"uuid": uuid, "targetURL": urlDict[uuid]}
    print(urlDict)
    if uuid in urlDict:
        return RedirectResponse(urlDict[uuid])
    return "nie działa"
    

@app.get("/typer")
def redirect_typer():
    return RedirectResponse("https://typer.tiangolo.com")

@app.get("/readdictionary/")
def read_dictionary():
    return urlDict