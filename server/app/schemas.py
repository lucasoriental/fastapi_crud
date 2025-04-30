from pydantic import BaseModel

class AlunoBase(BaseModel):
    matricula: int
    nome: str
    idade: int
    sexo: str
    email: str


class AlunoCreate(AlunoBase):
    pass

class Aluno(AlunoBase):
    id: int

    class config:
        from_attribute: True