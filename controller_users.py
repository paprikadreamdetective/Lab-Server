from controller import App
from typing import Union


app = App()

@app.get('/')
def read_root():
    return {'hello' : 'world'}

@app.get('/items/{items_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id' : item_id, 'q':q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}