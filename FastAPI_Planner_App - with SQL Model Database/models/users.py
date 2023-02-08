"""
    users.py: This file will contain the model definition for user operations.
"""

from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event



class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]
    
    
    class Config:
        schema_extra = {
            'example' : {
                'email': 'mklomo@icloud.com',
                'username': "marv",
                'events': []
            }
        }
        


class UserSignIn(User):
    email: EmailStr
    password: str
    
    
    class Config:
        schema_extra = {
            'example' : {
                'email': 'mklomo@icloud.com',
                'username': "marv",
                'events': []
            }
        }


class NewUser(BaseModel):
    email: str
    password: str
    