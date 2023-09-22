from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union
from sqlalchemy.orm import relationship
from model.evento import Evento
from model.pessoa import Pessoa

from  model import Base


class RotinaPadrao(Base):
    __tablename__ = 'rotinapadrao'

    id = Column("pk_rotinapadrao", Integer, primary_key=True)
    hora = Column(String(140), unique=False)
    diasemana = Column(String(140), unique=False)
    id_evento = Column(Integer, ForeignKey("evento.pk_evento"), nullable=False)
    id_pessoa = Column(Integer, ForeignKey("pessoa.pk_pessoa"), nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())

    evento = relationship("Evento")
    
    
    def __init__(self, hora:str, diasemana:str, id_evento:int, id_pessoa:int, data_insercao:Union[DateTime, None] = None):
        """
        Cria uma Rotina Padrão

        Arguments:
            hora: Hora de execução do evento
            diasemana: Dia da semana
            id_evento: Id do evento
            id_pessoa: Id da pessoa
        """
        self.hora = hora
        self.diasemana = diasemana
        self.id_evento = id_evento
        self.id_pessoa = id_pessoa

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
