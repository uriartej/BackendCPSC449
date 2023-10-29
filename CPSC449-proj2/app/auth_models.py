from pydantic import BaseModel


class Users(BaseModel):
    id: int
    username: str
    password: str
    roles: str


class RegisterUserRequest(BaseModel):
    username: str
    password: str
    roles: str


class VerifyUserRequest(BaseModel):
    username: str
    password: str
