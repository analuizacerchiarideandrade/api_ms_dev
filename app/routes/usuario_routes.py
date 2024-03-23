from typing import List
from fastapi import APIRouter, Response, Depends, status, Query, HTTPException
from sqlalchemy.orm import Session
from db.database import engine,SessionLocal, get_db
from db.models import Usuarios as UsuariosModel
from schemas.usuario import Usuarios as UsuariosSchema

from db.base import Base


#cria a tabela
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/usuarios")



@router.post("/addComSchema", status_code=status.HTTP_201_CREATED, description='Adicionar user')
def add_user(request:UsuariosSchema, db: Session = Depends(get_db)):
        # produto_on_db = ProdutosModel(id=request.id, item=request.item, peso=request.peso, numero_caixas=request.numero_caixas)
        user_on_db_ = UsuariosModel(**request.dict())
        db.add(user_on_db_)
        db.commit()
        db.refresh(user_on_db_)
        return user_on_db_