from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a data contract, only accept a JSON object that matches this structure
class User(BaseModel):
    name: str
    age: int
    favorite_food: str
    
# Use POST to recieve data in the body
@app.post("/user/")
def greet_user(user: User):  # tell FastAPI  that JSON object has to match User model
    return {
        "message": f"Hellow {user.name}, {user.age}, who loves {user.favorite_food}"
        }