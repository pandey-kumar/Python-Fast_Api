from pydantic import BaseModel

class MenuItemModel(BaseModel):
    id:int
    name:str
    category:str
    price:float
    description:str
    available:bool



#  Lets make a standard response  model

class MenuResponseModel(BaseModel):
    status:str ="Success"
    count:int
    items:list[MenuItemModel]


