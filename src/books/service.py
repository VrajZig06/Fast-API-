from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.validationSchema import BookCreate,BookUpdate
from src.books.models import Book
from datetime import datetime
from sqlmodel import select,desc
from fastapi import HTTPException,status

class BookService:
    # Get All Books 
    async def get_all_books(self,session:AsyncSession):
        try:
            statement = select(Book).order_by(desc(Book.created_at))
            result = await session.exec(statement)
            return result.all()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Error : {e}")

    # Get Single Book using ID 
    async def get_book(self,book_id:str,session:AsyncSession):
        try:
            statement  = select(Book).where(Book.id==book_id)
            result = await session.exec(statement)
            book =  result.first()
            return book if book is not None else None
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Error : {e}")
    
    # Delete Single Book using ID
    async def delete_book(self,book_id:str,session:AsyncSession):
        try:
            book_to_delete = await self.get_book(book_id,session)

            if book_to_delete is not None:
                await session.delete(book_to_delete)
                await session.commit()
                return True
            else:
                return False
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Error : {e}")
        
    # Update Book by ID and New Data
    async def update_book(self,book_id:str,book:BookUpdate,session:AsyncSession):
        try:
            book_to_update = await self.get_book(book_id,session)
            updated_data_dict = book.model_dump()
            
            if book_to_update is not None:
                for key,value in updated_data_dict.items():
                    setattr(book_to_update, key, value)

                await session.commit()
                return book_to_update
            else:
                return None
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Error : {e}")
        
    # Add New Book Details 
    async def add_book(self,book:BookCreate,session:AsyncSession):
        try:
            book_data_dict = book.model_dump()
            new_book = Book(**book_data_dict)
            new_book.published_date = datetime.strptime(str(book_data_dict['published_date']),"%Y-%m-%d").date()
            session.add(new_book)
            await session.commit() 
            return new_book
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Error : {e}")
