from fastapi import APIRouter, Path, HTTPException, status
from model import Todo, TodoItem, TodoItems


todo_router = APIRouter()



todo_list = []


# Insert new TODO and update the status code to 201 when successful
@todo_router.post('/todo', status_code = 201)
async def add_todo(todo: Todo) -> dict:
    """Add a new todo to the list

    Args:
        todo (dict): new todos

    Returns:
        dict: A message that tells success
    """
    todo_list.append(todo)
    return {'message': 'Todo added successfully'}


@todo_router.get('/todo', response_model=TodoItems)
async def get_todo() -> dict:
    """Returns all todos in the list

    Returns:
        dict: todo list
    """
    return {'todos': todo_list}



# Router with a path parameter todo_id
@todo_router.get('/todo/{todo_id}')
async def get_single_todo(todo_id: int = Path(..., title='The ID of the todo to retrieve')) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {'todo': todo}
        
    raise HTTPException(
                        status_code = status.HTTP_404_NOT_FOUND,
                        DETAIL = 'TODO with supplied ID does not exist'
                        )



# Update the todo router
@todo_router.put('/todo/{todo_id}')
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title='The ID of the TODO tp be updated')) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {'message': 'Todo Updated Successfully'}
        
    return {'message': 'Todo with Supplied ID does not exist'}


# Delete the todo with specified ID
@todo_router.delete('/todo/{todo_id}')
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"message": "Todo deleted successfully"}
        
    return {'message': 'Todo with supplied ID doe not exist'}

