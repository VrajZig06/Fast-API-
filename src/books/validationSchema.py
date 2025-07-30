from pydantic import BaseModel,Field,field_validator
from typing import Union,Optional,Any
from datetime import date,datetime
from uuid import UUID

# validation Pydantic Class at the time of Add New Book 
class BookInput(BaseModel):
    id : Optional[UUID] = None
    title : str = Field(min_length=3,max_length=50)
    author : str = Field(min_length=3,max_length=50)
    publisher : str = Field(min_length=3,max_length=50)
    page_count : int
    language : str

    @field_validator("language")
    def check_language_is_valid(cls,v):
        if v not in ['English',"Hindi","Gujarati"]:
            raise ValueError("Language Must be Valid.")
        
        return v
    
    @field_validator("page_count")
    def check_page_count(cls,v):
        if v < 0 and not v.isNumberic():
            raise ValueError("Page Count needs to Valid.")
        
        return v

#  Validation Pydantic Class at the time of Update Book Record
class BookUpdate(BaseModel):
    title : str = Field(min_length=3,max_length=50)
    author : str = Field(min_length=3,max_length=50)
    publisher : str = Field(min_length=3,max_length=50)
    page_count : int
    language : str


    @field_validator("language")
    def check_language_is_valid(cls,v):
        if v not in ['English',"Hindi","Gujarati"]:
            return ValueError("Language Must be Valid.")
        return v
    
    @field_validator("page_count")
    def check_page_count(cls,v):
        if v < 0 and not v.isNumberic():
            return ValueError("Page Count needs to Valid.")
        
        return v
    
# Validation Pydantic Class at the time of Giving Response from API
class APIResponse(BaseModel):
    Status : int
    Msg: str
    Data : Any

# Postgres Models Pydantic Models

class BookSchema(BaseModel):
    id : UUID
    title : str
    author : str
    publisher : str
    published_date : str
    page_count : int
    language : str
    created_at : datetime
    updated_at : datetime

class BookCreate(BaseModel):
    title : str 
    author : str 
    publisher : str 
    published_date : date
    page_count : int
    language : str

class BookUpdateSchema(BaseModel):
    title : str 
    author : str 
    publisher : str 
    page_count : int
    language : str

