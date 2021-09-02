from fastapi import FastAPI, Path, HTTPException, status, Query
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class Item (BaseModel):
    name : str
    price: float
    brand : Optional[str] = None

class UpdateItem (BaseModel):
    name : Optional[str] = None
    price: Optional[float] =None
    brand : Optional[str] = None

inventory = {}

@app.get('/get-item/{item_id}')
def get_item(item_id : int = Path(None, description='The Id of Item you like to View')):
    return inventory[item_id]


@app.get("/get-by-name")
def get_item(name : str = Query(None, title='Name', description='Name of Item')):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
        # return {'Msg':'Data Not Found'}
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        raise HTTPException(status_code=404, detail='Item  not Found')
    raise HTTPException(status_code=404, detail='Item  not Found')

@app.post('/create-item/{item_id}')
def create_item(item_id : int, item: Item):
    if item_id in inventory:
        # return {'Error': 'Item Id Already Exists'}
        raise HTTPException(status_code=404, detail='Item Id Already Exists')
    # inventory[item_id] = {'name': item.name, 'brand': item.brand, 'price':item.price}
    inventory[item_id] = item
    return inventory[item_id]

@app.put('/update-item/{item_id}')
def update_item(item_id : int, item: UpdateItem):
    if item_id not in inventory:
        # return {'Error': 'Item Id doesnot Exists'}
        raise HTTPException(status_code=404, detail='Item  Id Doesnot Exist')

    if item.name != None:
        inventory[item_id].name = item.name

    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]

@app.delete('/delete-item/{item_id}')
def delete_item(item_id : int):
    if item_id not in inventory:
        # return {'Error': 'Item Id doesnot Exists'}
        raise HTTPException(status_code=404, detail='Item  Id Doesnot Exist')
    del inventory[item_id]
    return {'Msg': 'Item Deleted Sucessfully'}