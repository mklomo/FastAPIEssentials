"""
    users.py: This file will handle routing operations such as the registration and
    signing-in of users.
"""
from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn, NewUser


user_router = APIRouter(
                           tags=['User'] ,
                        )


# In app database
users = {}


# Implement the sign-in code
@user_router.post('/signup')
async def sign_new_user(data: NewUser):
    if data.email in users:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail='Username already exists'
        )
    elif data.email is not None and data.password is not None:
        users[data.email] = data
        return {
                'message': 'User successfully registered'
                }
        
    else:
        return {'message': 'Please check username or password entered'}
        
        
        
# Sign-in route
@user_router.post('/signin')
async def sign_user_in(user: UserSignIn) -> dict:
    if users[user.email] not in users:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail='User does not exist'
        )
        
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail='Wrong Credentials Passed'
        )
        
    return {
        'message': 'User signed in successfully'
    }
