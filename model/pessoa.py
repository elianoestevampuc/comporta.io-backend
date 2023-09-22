from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Evento


class Pessoa(Base):
    __tablename__ = 'pessoa'

    id = Column("pk_pessoa", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre a pessoa e o evento.
    eventos = relationship("Evento")


    def __init__(self, nome:str, data_insercao:Union[DateTime, None] = None):
        """
        Cria uma Pessoa

        Arguments:
            nome: Nome da pessoa
        """
        self.nome = nome

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao


    def adiciona_evento(self, evento:Evento):
        """ Adiciona um novo evento a Pessoa
        """
        self.eventos.append(evento)
     
