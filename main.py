from fastapi import FastAPI
from typing import List, Optional
from enum import IntEnum
from pydantic import BaseModel, Field
api = FastAPI()

all_todos = [
    {'todo_id': 1, 'todo_name': 'Sports', "todo_description": "Go to the gym"},
    {'todo_id': 2, 'todo_name': 'Read', "todo_description": "Read 10 pages"},
    {'todo_id': 3, 'todo_name': 'Shop', "todo_description": "Go shopping"},
    {'todo_id': 4, 'todo_name': 'Study', "todo_description": "Study for the examn"},
    {'todo_id': 5, 'todo_name': 'Meditate', "todo_description": "Meditate 20 minutes"},
]




# GET, POST, PUT, DELETE


@api.get("/")
def index():
    return {'message': 'Hello World'}
#GET Method
@api.get("/todos/{todo_id}")
def get_todo(todo_id):
    for todo in all_todos: 
        if todo['todo_id'] == int(todo_id):
            return {'result': todo}
#Path Parameter
@api.get("/todoss")
def get_all_todos():
    return {'result': all_todos}
    
#Query Parameter
@api.get('/todos')
def get_todos(first_n: int = None):
    if first_n: 
        return all_todos[:first_n]
    return all_todos

#POST Method
@api.post('/todos')
def create_todo(todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1
    new_todo = {
        'todo_id': new_todo_id,
        'todo_name': todo['todo_name'],
        'todo_description': todo['todo_description']
    }
    all_todos.append(new_todo)
    return new_todo

#PUT Method
@api.put('/todos/{todo_id}')
def update_todo(todo_id: int, updated_todo: dict):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            todo['todo_name'] = updated_todo.get('todo_name', todo['todo_name'])
            todo['todo_description'] = updated_todo.get('todo_description', todo['todo_description'])
            return todo
    return {'message': 'Todo not found'}

#DELETE Method
@api.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo['todo_id'] == todo_id:
            deleted_todo = all_todos.pop(index)
            return {'message': 'Todo deleted', 'todo': deleted_todo}
    return {'message': 'Todo not found'}


#Writing good code