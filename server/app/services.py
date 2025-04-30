from database_model import Alunos
from sqlalchemy.orm import Session
from schemas import AlunoCreate

def create_aluno(db: Session, data: AlunoCreate):
    aluno_instance = Alunos(**data.model_dump())
    db.add(aluno_instance)
    db.commit()
    db.refresh(aluno_instance)
    return aluno_instance

def get_alunos(db: Session):
    return db.query(Alunos).all()

def get_aluno(db: Session, aluno_id: int):
    return db.query(Alunos).filter(Alunos.id == aluno_id).first()

def update_aluno(db: Session, aluno_id: int, data: AlunoCreate):
    aluno_queryset = db.query(Alunos).filter(Alunos.id == aluno_id).first()
    if aluno_queryset:
        for key, value in data.model_dump().items():
            setattr(aluno_queryset, key, value)
        db.commit()
        db.refresh(aluno_queryset)
    return aluno_queryset

def delete_aluno(db: Session, aluno_id: int):
    aluno_queryset = db.query(Alunos).filter(Alunos.id == aluno_id).first()
    if aluno_queryset:
        db.delete(aluno_queryset)
        db.commit()
    return aluno_queryset