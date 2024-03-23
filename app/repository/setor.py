from sqlalchemy.orm import Session

from db.models import Setores

class SetorRepository:
    @staticmethod
    def find_all(db: Session) -> list[Setores]:
        return db.query(Setores).all()

    @staticmethod
    def save(db: Session, setor: Setores) -> Setores:
        if setor.id:
            db.merge(setor)
        else:
            db.add(setor)
        db.commit()
        return setor

    @staticmethod
    def find_by_id(db: Session, id: int) -> Setores:
        return db.query(Setores).filter(Setores.id == id).first()
 
    @staticmethod
    def find_by_nome_item(db: Session, nome_item: str) -> Setores:
        return db.query(Setores).filter(Setores.item == nome_item).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Setores).filter(Setores.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        setor = db.query(Setores).filter(Setores.id == id).first()
        if setor is not None:
            db.delete(setor)
            db.commit()