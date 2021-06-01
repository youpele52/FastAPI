# creating base route
from fastapi import FastAPI
app = FastAPI()

# minimal app -- get request


@app.get("/", tags=["Root"])
# the root func points to a dictionary
async def root() -> dict:
    # you can return anything, however fastapi will convert it ti JSON
    return {"Ping": "Pong"}


# Get request: Read Todo list
@app.get('/todos', tags=['todos'])
async def get_todo() -> dict:
    # the data being return here could be from a database
    # here a simple dictionary emulating a database is used
    return {"data": todos}


# Post request: Create Todo item in todo list
@app.post('/todos', tags=['todos'])
# the arg is a todo inform of a dict, which is the data type we are expecting
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {"data": "A todo has been added successfully!"}


# Put request: Update an item in todo list
@app.put('/todos/{id}', tags=['todos'])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            # todo['Activity'] = body['Activity']
            # todo['TargetTime'] = body['TargetTime']
            todos[todos.index(todo)] = body
            return {'data': f"Todo with the id {id} has been successfully updated!"
                    }
    return {'data': f"Todo with this id number {id} was not found!"
            }


# Delete : delete item from todo list
@app.delete('/todos/{id}', tags=['todos'])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todos.remove(todo)
            return {'data': f"Todo with the id {id} has been deleted!"
                    }
    return {"data": f"Todo with this id number {id} was not found!"}


todos = [
    {
        "id": "2",
        "Activity": "Program a MERN or FARM web app.",
        "TargetTime": "Undecided"
    },
    {
        "id": "1",
        "Activity": "Plan for your holiday",
        "TargetTime": "3 June 2021"
    }
]
