from pydantic import BaseModel,field_validator

class PincodeRequestModel(BaseModel):
    pincode:str

    # Lets writea validator for pincode to be 0f 6digits only
    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls,value):
        if len(value)!=6 or not value.isdigit():
            raise ValueError("Pincode must be of 6 digit and a number")
        return value


class LocationResponseModel(BaseModel):
    pincode:str
    city:str
    state:str
    district:str


#  Lets make mode also for bulk Request and responses as well

class BulkPincodeRequest(BaseModel):
    pincodes:list[str]

    @field_validator("pincodes")
    @classmethod
    def validate_pincodes(cls,values):
        if len(values)==0:
            raise ValueError("At least one pin code is required")
        if len(values)>20:
            raise ValueError("Maximum 20 pin codes allowed per request")
        for pincode in values:
            if len(pincode)!=6 or not pincode.isdigit():
                raise ValueError("Each pincode must be of six digits")
        return values


class BulkLocationReponseModel(BaseModel):
    status: str="Success"
    found:int
    not_found:int
    result:list[LocationResponseModel]
    missing:list[str]
