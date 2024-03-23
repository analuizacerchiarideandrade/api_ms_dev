from typing import List
from fastapi import APIRouter, Response, Depends, status, Query, HTTPException
from sqlalchemy.orm import Session
from db.database import engine,SessionLocal, get_db
from db.models import Produtos as ProdutosModel
from schemas.produto import Produtos, ProdutoRequest, ProdutoResponse
from sqlalchemy.orm import Session
from repository.produto import ProdutoRepository


from db.base import Base
from db.database import get_db


#cria a tabela
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/v1/api/produtos")


@router.post("/criar", response_model=ProdutoResponse, status_code=status.HTTP_201_CREATED)
def create(request: ProdutoRequest, db: Session = Depends(get_db)):
    produto = ProdutoRepository.save(db, ProdutosModel(**request.dict()))
    return ProdutoResponse.from_orm(produto)


@router.get("/listar_todos", response_model=list[ProdutoResponse])
def find_all(db: Session = Depends(get_db)):
    produtos = ProdutoRepository.find_all(db)
    return [ProdutoResponse.from_orm(produto) for produto in produtos]


@router.get("/procurar_por_id/{id}", response_model=ProdutoResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    produto = ProdutoRepository.find_by_id(db, id)
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    return ProdutoResponse.from_orm(produto)


@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not ProdutoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    ProdutoRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/update/{id}", response_model=ProdutoResponse)
def update(id: int, request: ProdutoRequest, db: Session = Depends(get_db)):
    if not ProdutoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    produto = ProdutoRepository.save(db, ProdutosModel(id=id, **request.dict()))
    return ProdutoResponse.from_orm(produto)