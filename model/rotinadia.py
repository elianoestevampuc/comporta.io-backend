from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean, Date
from datetime import datetime
from typing import Union

from  model import Base


class RotinaDia(Base):
    __tablename__ = 'rotinadia'

    id = Column("pk_rotinadia", Integer, primary_key=True)
    hora = Column(String(140), unique=False)
    id_evento = Column(Integer, ForeignKey("evento.pk_evento"), nullable=False)
    id_pessoa = Column(Integer, ForeignKey("pessoa.pk_pessoa"), nullable=False)
    executou = Column(Boolean, unique=False)
    data_execucao = Column(DateTime, default=datetime.now())
    data_insercao = Column(DateTime, default=datetime.now())

    
    def __init__(self, hora:str, id_evento:int, id_pessoa:int, executou:Boolean, data_execucao:DateTime, data_insercao:Union[DateTime, None] = None):
        """
        Cria uma Rotina Dia

        Arguments:
            hora: Hora de execução do evento
            id_evento: Id do evento
            id_pessoa: Id da pessoa
            executou: Boleano para indicar se foi executado ou não
        """
        self.hora = hora
        self.id_evento = id_evento
        self.id_pessoa = id_pessoa
        self.executou = executou
        self.data_execucao = data_execucao

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
