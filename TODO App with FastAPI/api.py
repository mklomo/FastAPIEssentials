from fastapi import FastAPI
from todo import todo_router


# Instantiate the app
app = FastAPI()


# Create a welcome route
@app.get('/')
async def welcome() -> dict:
    return {'message': 'Hello World'}



# Include the todo_router
app.include_router(todo_router)