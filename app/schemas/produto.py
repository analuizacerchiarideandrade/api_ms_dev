from pydantic import BaseModel
from pydantic import validator
import re

#TODO criar pasta caso de uso
# #Este arquivo ficam as regras de negócio

class Produtos(BaseModel):
    item: str
    peso: float
    numero_caixas: int
    id_setor: int

    @validator('peso')
    def validate_peso(cls, value):
        if value <= 0:
            raise ValueError('Peso Invalido')
        return value

    @validator('item')
    def validate_item(cls, value):
        if not re.match('^([a-z]|-|_)+$', value):
            raise ValueError('Invalid item')
        return value


class ProdutoRequest(Produtos):
    item: str
    peso: float
    numero_caixas: int
    id_setor: int


class ProdutoResponse(Produtos):
    id: int
    item: str
    peso: float
    numero_caixas: int
    id_setor: int

    class Config:
        from_attributes=True    
        orm_mode = True