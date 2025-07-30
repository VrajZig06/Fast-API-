from fastapi import APIRouter,HTTPException,status,Depends
from src.books.book_data import Books
from src.books.validationSchema import BookInput,APIResponse,BookCreate,BookUpdateSchema
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from ..utils.Response import Response
from src.books.service import BookService
import uuid
from uuid import UUID

bookRouter = APIRouter()
bookService = BookService()

# Get All Books
@bookRouter.get("/")
async def get_all_books(session:AsyncSession = Depends(get_session)):
    try:
       books = await bookService.get_all_books(session)
       return APIResponse(Status=status.HTTP_200_OK,Msg="All Books Fetched Successfully",Data=books)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Error : {e}")

# ----- Past Code ----
# @bookRouter.get("/",response_model=APIResponse)
# def get_all_books() -> dict:
#     try:
#        return Response(status=200,msg="All Books Record Fetched Succesfully",data=Books)
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Error : {e}")
    

# Add new Book Details to Books
@bookRouter.post("/add")
async def add_book(book:BookCreate,session:AsyncSession = Depends(get_session)):
    try:
         new_book = await bookService.add_book(book,session)
         return APIResponse(Status=status.HTTP_201_CREATED,Msg="New Book Created Successfully",Data=new_book)    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Error : {e}")
    
# ----- Past Code ----
# @bookRouter.post("/add",status_code=status.HTTP_201_CREATED,response_model=APIResponse)
# def add_book(book:BookInput):
#     try:
#         book.id =uuid.uuid4()
#         Books.append(book.model_dump())
#         return Response(status=201,msg="Book Addedd Successfully!",data=book)
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Error : {e}")


# Get individual Book Detail
@bookRouter.get("/{book_id}")
async def get_book(book_id: UUID,session:AsyncSession = Depends(get_session)):
    try:
        book = await bookService.get_book(book_id,session)
        if book is not None:
         return APIResponse(Status=status.HTTP_200_OK,Msg=f"Book with Given ID Fetched Successfully",Data=book) 
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error: {e}"
        )

# ----- Past Code ----
# @bookRouter.get("/{book_id}", response_model=APIResponse)
# def get_book(book_id: UUID):
#     try:
#         if not Books:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail="Books Not Available"
#             )

#         for book in Books:
#             if book['id'] == book_id: 
#                 return APIResponse(
#                     Status=200,
#                     Msg="Book Found Successfully",
#                     Data=book
#                 )

#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Book Not Found"
#         )

#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail=f"Error: {e}"
#         )
    
# Update Individual Book Detail
@bookRouter.patch("/{book_id}")
async def update_book(book_id:UUID,book: BookUpdateSchema,session:AsyncSession = Depends(get_session)):
    try:
        updatedBook = await bookService.update_book(book_id,book,session)
        if updatedBook is not None:
            return APIResponse(Status=status.HTTP_200_OK,Msg="Book Updated Successfully",Data=updatedBook)
        else:
            return None
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")

# ----- Past Code ----
# @bookRouter.patch("/{book_id}")
# def update_book(book_id:UUID,book: BookInput):
#     try:
#         if not Books:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Books Not Available")

#         for index, existing_book in enumerate(Books):
#             if existing_book['id'] == book_id:
#                 updated_book = {
#                     "id": book_id,
#                     "title": book.title,
#                     "author": book.author,
#                     "publisher": book.publisher,
#                     "page_count": book.page_count,
#                     "language": book.language
#                 }
#                 Books[index] = updated_book
#                 return Response(status=200, msg="Book Updated Successfully", data=updated_book)

#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found with this ID")
    
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")


# Delete Book Details by ID
@bookRouter.delete("/{book_id}")
async def delete_book(book_id:UUID,session:AsyncSession = Depends(get_session)):
    try:
        isDeleted = await bookService.delete_book(book_id,session)
        if isDeleted:
            return APIResponse(Status=status.HTTP_200_OK,Msg="Book Deleted Successfully",Data=None)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book Not Found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Error : {e}")
    
# ----- Past Code ----
# @bookRouter.delete("/{book_id}")
# def delete_book(book_id:UUID):
#     try:
#         if not Books:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Books Not Available")
    
#         for index,book in enumerate(Books):
#             if book['id'] == book_id:
#                 Books.pop(index)
#                 return Response(status=200,msg="Book Deleted Successfully",data=None)
#             else:
#                 raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book Not Found with this ID")
        
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Error : {e}")