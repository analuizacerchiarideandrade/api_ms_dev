import re
from pydantic import validator, EmailStr, BaseModel
from datetime import datetime


class Usuarios(BaseModel):
    username: str
    password: str
    email: EmailStr

    @validator('username')
    def validate_username(cls, value):
        if not re.match('^([a-z]|[A-Z]|[0-9]|-|_|@)+$', value):
            raise ValueError('Invalid username')
        return value

class UsuarioSaida(BaseModel):
    username: str
    email: EmailStr