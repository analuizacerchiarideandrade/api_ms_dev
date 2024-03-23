from typing import List
from fastapi import APIRouter, Response, Depends, status, Query
from sqlalchemy.orm import Session
from db.database import engine,SessionLocal, get_db
from db.models import Setores as SetorModel
from schemas.setor import Setores, SetorRequest, SetorResponse
from sqlalchemy.orm import Session
from repository.setor import SetorRepository


from db.base import Base
from db.database import get_db


#cria a tabela
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/v1/api/setores")


@router.post("/criar", response_model=SetorResponse, status_code=status.HTTP_201_CREATED)
def create(request: SetorRequest, db: Session = Depends(get_db)):
    setor = SetorRepository.save(db, SetorModel(**request.dict()))
    return SetorResponse.from_orm(setor)


@router.get("/listar_todos", response_model=list[SetorResponse])
def find_all(db: Session = Depends(get_db)):
    setores = SetorRepository.find_all(db)
    return [SetorResponse.from_orm(setor) for setor in setores]


@router.get("/procurar_por_id/{id}", response_model=SetorResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    setor = SetorRepository.find_by_id(db, id)
    if not setor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Setor não encontrado"
        )
    return SetorResponse.from_orm(setor)


@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not SetorRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Setor não encontrado"
        )
    SetorRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/update/{id}", response_model=SetorResponse)
def update(id: int, request: SetorRequest, db: Session = Depends(get_db)):
    if not SetorRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Setor não encontrado"
        )
    setor = SetorRepository.save(db, SetorModel(id=id, **request.dict()))
    return SetorResponse.from_orm(setor)