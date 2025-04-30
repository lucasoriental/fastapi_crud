from database import Base
from sqlalchemy import Integer, String, Column

class Alunos(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, nullable=False)
    matricula = Column(Integer, nullable=False)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    sexo = Column(String, nullable=False)
    email = Column(String, nullable=False)