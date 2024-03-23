
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, func
from sqlalchemy.orm import relationship
from db.base import Base
from sqlalchemy_utils import EmailType


class Produtos(Base):
    __tablename__ = "tb_produtos"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    item = Column('item', String, nullable=False)
    peso = Column('peso', Float)
    numero_caixas = Column('numero_caixas', Integer)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, onupdate=func.now())
    id_setor =Column('id_setor', ForeignKey('tb_setores.id'), nullable=False)
  


class Setores(Base):
    __tablename__ = 'tb_setores'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String, nullable=False)



class Usuarios(Base):
    __tablename__ = 'tb_usuarios'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)
    email = Column('Email', EmailType)
