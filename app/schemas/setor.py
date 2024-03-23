from pydantic import BaseModel
from pydantic import validator
import re

#TODO criar pasta caso de uso
# #Este arquivo ficam as regras de negócio

class Setores(BaseModel):
    id: int
    nome: str

    @validator('nome')
    def validate_peso(cls, value):
        if len(value) <= 0:
            raise ValueError('Nome Invalido')
        return value

class SetorRequest(Setores):
    id: int
    nome: str

class SetorResponse(Setores):
    id: int
    nome: str

    class Config:
        from_attributes=True    
        orm_mode = True