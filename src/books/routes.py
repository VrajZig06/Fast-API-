from fastapi import APIRouter,HTTPException,status
from src.books.book_data import Books
from src.books.validationSchema import BookInput,APIResponse
from ..utils.Response import Response
import uuid
from uuid import UUID

bookRouter = APIRouter()

# Get All Books
@bookRouter.get("/",response_model=APIResponse)
def get_all_books():
    try:
       return Response(status=200,msg="All Books Record Fetched Succesfully",data=Books)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Error : {e}")
    

# Add new Book Details to Books
@bookRouter.post("/add",status_code=status.HTTP_201_CREATED,response_model=APIResponse)
def add_book(book:BookInput):
    try:
        book.id =uuid.uuid4()
        Books.append(book.model_dump())
        return Response(status=201,msg="Book Addedd Successfully!",data=book)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Error : {e}")


# Get individual Book Detail
@bookRouter.get("/{book_id}", response_model=APIResponse)
def get_book(book_id: UUID):
    try:
        if not Books:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Books Not Available"
            )

        for book in Books:
            if book['id'] == book_id: 
                return APIResponse(
                    Status=200,
                    Msg="Book Found Successfully",
                    Data=book
                )

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book Not Found"
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error: {e}"
        )
    
# Update Individual Book Detail
@bookRouter.patch("/{book_id}")
def update_book(book_id:UUID,book: BookInput):
    try:
        if not Books:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Books Not Available")

        for index, existing_book in enumerate(Books):
            if existing_book['id'] == book_id:
                updated_book = {
                    "id": book_id,
                    "title": book.title,
                    "author": book.author,
                    "publisher": book.publisher,
                    "page_count": book.page_count,
                    "language": book.language
                }
                Books[index] = updated_book
                return Response(status=200, msg="Book Updated Successfully", data=updated_book)

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found with this ID")
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")


# Delete Book Details by ID
@bookRouter.delete("/{book_id}")
def delete_book(book_id:UUID):
    try:
        if not Books:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Books Not Available")
    
        for index,book in enumerate(Books):
            if book['id'] == book_id:
                Books.pop(index)
                return Response(status=200,msg="Book Deleted Successfully",data=None)
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book Not Found with this ID")
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Error : {e}")