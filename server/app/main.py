from fastapi import FastAPI, Depends, HTTPException
import services, database_model, schemas
from database import get_db, engine
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/alunos/", response_model= list[schemas.Aluno])
def get_all_alunos(db: Session = Depends(get_db)):
    return services.get_alunos(db)

@app.get("/alunos/{id}", response_model= schemas.Aluno)
def get_aluno_by_id(id: int, db: Session = Depends(get_db)):
    aluno_queryset = services.get_aluno(db, id)
    if aluno_queryset:
        return aluno_queryset
    raise HTTPException(status_code=404, detail="Looks like this ID doesn't exist... Try another one!")
 
@app.post("/alunos/", response_model= schemas.Aluno)
def create_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    return services.create_aluno(db, aluno)

@app.put("/alunos/{id}", response_model= schemas.Aluno)
def update_aluno(id: int, aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    db_update = services.update_aluno(db, id, aluno)
    if not db_update:
        raise HTTPException(status_code=404, detail="Something went wrong... Try updating again!")
    return db_update

@app.delete("/alunos/{id}", response_model= schemas.Aluno)
def delete_aluno(id: int, db: Session = Depends(get_db)):
    delete_entry = services.delete_aluno(db, id)
    if delete_entry:
        return delete_entry
    raise HTTPException(status_code=404, detail="Something went wrong... Try deleting again!")