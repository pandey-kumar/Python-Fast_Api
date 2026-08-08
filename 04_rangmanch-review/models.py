from sqlmodel import SQLModel,Field
from typing import Optional
from datetime import datetime




# Table true specifies that it is a SQL RDBMS TABLE not a normal class
class Review(SQLModel,table=True):
    id:Optional[int] =Field(default=None,primary_key=True)
    play_name:str=Field(index=True)
    reviewer_name:str
    rating:int =Field(ge=1,le=5)
    comment:str
    created_at:datetime=Field(default_factory=datetime.now)



#  this is a normal validation class  (Create)
class ReviewCreate(SQLModel):
    play_name:str
    reviewer_name:str
    rating:int =Field(ge=1,le=5)
    comment:str



#  READ
class ReviewRead(SQLModel):  
    id:int
    play_name:str
    reviewer_name:str
    rating:int
    comment:str
    created_at:datetime



# UPDATE
class ReviewUpdate(SQLModel):
    rating:Optional[int]=Field(default=None,ge=1,le=5)
    comment:Optional[str]=None
