from fastapi import FastAPI
from fastapi import Request

# Lets design a production grade description :-

app=FastAPI(
    title="Welcome to the Fast API docs",
    summary="Here you will get a basic overview of fast api",
    description="This is a complete fast api guide from basic to advanced",
    version="1.0.0.2",
    docs_url="/mydocs",
    redoc_url="/myredocs",
    openapi_url="/openapi.json"
)




@app.get("/")
def home_route():
    #  fast api automatically converts python dict to json format
    """Here you can get home route"""
    return {
        "message":"Welcome to the home route",
        "status":"Healthy"
    }


@app.get("/about")
def about_page():
    """You can get meta data from here """
    return{
        "message":"Welcome to the about page",
        "status":"200 ok",
        "description":"This is about page"
    }

#  Lets write some more routes sending array of objects etc

@app.get("/orders")
def get_orders():
    """To get the order details """
    return {
            "orders":[
            {"id":1,"name":"butter chicken","status":"delivered"},
            {"id":2,"name":"paneer pakoda","status":"pending"},
            {"id":3,"name":"masala Dosa","status":"delivered"},
            ]
    }

#  starlet automatically understoods the route 
@app.get("/orders/status")
def get_order_status():
    """To get the order status """
    return{
        "Total orderes":2_34_723,
        "status":"200 ok",
        "Top city":"begaluru"
    }


#  Lets get the request info that client is giving :-


@app.get("/debug/request-info")
async def get_request_info(request:Request):
    """Inspect the raw request object """
    return {
        "method":request.method,
        "url":str(request.url),
        "headers":dict(request.headers),
        "path-params":request.path_params,
        "query-params":dict(request.query_params)
    }



# Lets Learn Docs Creation in better manner

# You can add several things while docs creation :-

# We can group the things into diffrent sections

@app.get(
    "/orders/active",
    summary="This will demonstrate the active orders",
    description="active orders description",
    tags=["Orders"],
    response_description="Reponse of active orders",
    deprecated=False

)
def get_active_orders():
    """This docstring also appear in the docs"""
    return {
        "active Orders":[
            {"id":1,"item":"utensils","status":"Delivered"},
        ]

    }


# Lets take example of restraunt :-

@app.get("/restaurants" , tags=["restaurant"])
def list_restro():
    """This is restaurant list test """
    return {
        "test":"test"
    }