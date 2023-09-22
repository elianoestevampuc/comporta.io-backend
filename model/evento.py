from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from  model import Base


class Evento(Base):
    __tablename__ = 'evento'

    id = Column("pk_evento", Integer, primary_key=True)
    nome = Column(String(140), unique=False)
    data_insercao = Column(DateTime, default=datetime.now())
    pessoa = Column(Integer, ForeignKey("pessoa.pk_pessoa"), nullable=False)


    def __init__(self, nome:str, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Evento

        Arguments:
            nome: Nome do evento
        """
        self.nome = nome

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
