from datetime import datetime
from sqlalchemy import DateTime
from pydantic import BaseModel
from typing import List
from model.rotinadia import RotinaDia


class RotinaDiaSchema(BaseModel):
    """ Define como uma rotina dia deve ser representada.
    """    
    id_pessoa: int = 1
    id_evento: int = 1
    hora: str = "07:00"
    executou: bool = 1
    data_execucao: datetime = None


class RotinaDiaBuscaIdSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca pelo id.
    """    
    id: int = 1   


class RotinaDiaBuscaPessoaDiaExecucaoSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca pelo id da pessoa a data de execução.
    """    
    id_pessoa: int = 1   
    data_execucao: datetime = None


class RotinaDiaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    hora: str   


class ListagemRotinasDiaSchema(BaseModel):
    """ Define como uma listagem de rotinas dia será retornada.
    """
    rotinas:List[RotinaDiaSchema]       


def apresenta_rotinadia(rotinadia: RotinaDia):
    """ Retorna uma representação da rotina dia seguindo o schema definido em
        RotinaDiaViewSchema.
    """    
    return {
        "id": rotinadia.id,
        "hora": rotinadia.hora,
        "id_evento": rotinadia.id_evento,
        "id_pessoa": rotinadia.id_pessoa,
        "executou": rotinadia.executou
    }   


def apresenta_rotinasdia(rotinasdia: List[RotinaDia]):
    """ Retorna uma representação de rotinas dia seguindo o schema definido em
        RotinaDiaViewSchema.
    """
    result = []
    for rotinadia in rotinasdia:
        result.append({
            "id": rotinadia.id,
            "hora": rotinadia.hora,
            "id_evento": rotinadia.id_evento,
            "id_pessoa": rotinadia.id_pessoa,
            "executou": rotinadia.executou,
            "data_execucao": rotinadia.data_execucao.isoformat()
        })

    return {"rotinasdia": result} 