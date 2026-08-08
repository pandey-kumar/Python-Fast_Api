from fastapi import FastAPI
from data import pincode_db
from exceptions import(
    PincodeNotFoundError,
    pincode_not_found_handler,
    InvalidPincodeError,
    invalid_pincode_handler
)

from models import (
    PincodeRequestModel,
    LocationResponseModel,
    BulkPincodeRequest,
    BulkLocationReponseModel
)





app=FastAPI(
    title="Pincode Lookup API",
    description="Auto fill city and state from indian pincode during the checkout"
)


@app.get("/")
def root():
    return {"message":"Welcome to the Pincode Lookup API"}



# Firslty we would have to register the exceptions here :- add_exception_handler

app.add_exception_handler(PincodeNotFoundError,pincode_not_found_handler)
app.add_exception_handler(InvalidPincodeError,invalid_pincode_handler)


#  Lets handle the pincode and bulk routes



# access pincode using request body

@app.get("/pincode",response_model=LocationResponseModel)
def get_pincode_location_via_request(request:PincodeRequestModel):

    code=request.pincode

    if code not in pincode_db:
        raise PincodeNotFoundError(code,"This Pincode not found ")

    return pincode_db[code]


# access pincode using Path params

@app.get("/pincode/{code}", response_model=LocationResponseModel)
def get_pincode_location(code:str):
    if len(code)!=6 or not code.isdigit():
        raise InvalidPincodeError(code,"Code must be of 6 digits")

    if code not in pincode_db:
        raise PincodeNotFoundError(code,"Pin code not found")
    
    return pincode_db[code]


# Lets also handle the bulk route

# this will be post route Recieving the multiple codes

@app.post("/pincode/bulk",response_model=BulkLocationReponseModel)
def get_bulk_pincode_locations(request:BulkPincodeRequest):

   results=[]
   missing=[]

   for code in request.pincodes:
       if code in pincode_db:
           results.append(pincode_db[code])
       else:
           missing.append(code)

   
   return BulkLocationReponseModel(
       found=len(results),
       not_found=len(missing),
       result=results,
       missing=missing
   ) 



