from fastapi import FastAPI
from src.books.routes import bookRouter
from src.utils.Response import Response

# Run Command : fastapi ./src

app = FastAPI()

app.include_router(bookRouter,prefix="/book")

@app.get("/")
def root_route():
    return Response(status=200,msg="Welcome to Bookly",data=None)


