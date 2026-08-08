from fastapi import FastAPI, Query,HTTPException
from models import MenuResponseModel,MenuItemModel
from data import menu_items

app=FastAPI(
    title="Welcome to chai Menu API for web and mobile applications",
    description="This is API docs of the Chai Menu app"
)


@app.get("/")
def root():
    return {"message":"Welcome to the chai menu app"}


""" 
Note :-  "/menu"   This is path

"/menu?category="chai"&available=True  -> here after ?  

these are query params

for that we need Query

"""


# Here Dependency Injection is being done via response_model
# It tells that on this route reponse would be in the format of MenuItemModel


# @app.get("/menu",response_model=MenuResponseModel)
# def view_menu(category:str|None = Query(None,description="Filter by chai ,snacks , coffee,south_indian, main_course etc")):

#     if category:
#         filtered_items=[item for item in menu_items if item["category"]==category.lower()]

#         if not filtered_items:
#             raise HTTPException(status_code=404 , detail=f"No Itemsfound in the given category : {category}")
        
#         return MenuResponseModel(count=len(filtered_items),items=filtered_items)
    
#     return MenuResponseModel(count=len(menu_items),items=menu_items)


# @app.get("/menu/{item_id}",response_model=MenuItemModel)
# def get_menu_item(item_id:int):
#     for item in menu_items:
#         if item["id"]==item_id:
#             return item
#     raise HTTPException(status_code=404, detail=f"item not found for the Items id : {item_id}")




@app.get("/menu",response_model=MenuResponseModel)
def get_menu_items(category:str|None = Query(None,description="filter on the basis of categories")):
    if category:
        filter_items=[item for item in menu_items if item["category"]==category.lower()]
        if not filter_items:
            raise HTTPException(status_code=404, detail=f"item not found with category: {category}")
        return MenuResponseModel(count=len(filter_items),items=filter_items)

    return MenuResponseModel(count=len(menu_items),items=menu_items)


@app.get("/menu/{item_id}",response_model=MenuItemModel)
def get_menu_item(item_id:int):
    for item in menu_items:
        if item["id"]==item_id:
            return item
    raise HTTPException(status_code=404,detail=f"item not found for the item_id:{item_id}")
    