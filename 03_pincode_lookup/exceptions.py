from fastapi.responses import JSONResponse
from fastapi import Request


# Exception class 

class PincodeNotFoundError(Exception):
    def __init__(self, pincode:str):
        self.pincode=pincode


class InvalidPincodeError(Exception):
    def __init__(self, pincode : str ,reason:str ="Invalid Format"):
        self.pincode=pincode
        self.reason=reason


# class handlers

async def pincode_not_found_handler(request:Request, exptn:PincodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error":"Pincode not found",
            "message":f"No location for pincode : {exptn.pincode}",
            "pincode":exptn.pincode
        }
    )


async def invalid_pincode_handler(request:Request,exptn:InvalidPincodeError):
    return JSONResponse(
        status_code=400,
        content={
            "error":"Invalid pincode",
            "message":f"pincode {exptn.pincode} is invalid due to {exptn.reason}",
            "pincode":exptn.pincode
        }
    )
