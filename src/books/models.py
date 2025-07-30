from sqlmodel import SQLModel,Field,Column
from datetime import datetime
import sqlalchemy.dialects.postgresql as pg

import uuid 

class Book(SQLModel,table=True):
    __tablename__ = "books"

    id : uuid.UUID = Field(
        sa_column=Column(pg.UUID,nullable=False,primary_key=True,default=uuid.uuid4())
    )
    title : str
    author : str 
    publisher : str
    page_count : int
    language : str
    created_at : datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP(timezone=True),default=datetime.now
        )
    )
    updated_at : datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP(timezone=True),default=datetime.now
        )
    )

    def __repr__(self):
        return f"Book : {self.title}"