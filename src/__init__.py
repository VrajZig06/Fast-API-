from fastapi import FastAPI
from src.books.routes import bookRouter
from src.utils.Response import Response
from contextlib import asynccontextmanager
from src.db.main import init_db

# Run Command : fastapi ./src

# Run When Server Start and Stop
@asynccontextmanager
async def life_span(app:FastAPI):
    print("Server is Starting...")
    await init_db()
    yield # this is for differentiate starting of app and ending of app
    print("Server has been Stopped")

app = FastAPI(
    lifespan=life_span
)

app.include_router(bookRouter,prefix="/book")

@app.get("/")
def root_route():
    return Response(status=200,msg="Welcome to Bookly",data=None)


