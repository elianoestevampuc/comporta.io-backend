from pydantic import BaseModel
from datetime import datetime
from typing import List
from model.rotinapadrao import RotinaPadrao


class RotinaPadraoSchema(BaseModel):
    """ Define como uma rotina padrão deve ser representada.
    """
    id_pessoa: int = 1
    id_evento: int = 1
    hora: str = "07:00"
    diassemana: str = "seg,ter,qua"
    data_atual: datetime = None


class RotinaPadraoBuscaIdSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca pelo id.
    """
    id: int = 1   


class RotinaPadraoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    hora: str    


class ListagemRotinasPadraoSchema(BaseModel):
    """ Define como uma listagem de rotinas padrão será retornada.
    """
    rotinas:List[RotinaPadraoSchema]    


def apresenta_rotinapadrao(rotinapadrao: RotinaPadrao):
    """ Retorna uma representação de rotina padrão seguindo o schema definido em
        RotinaPadraoViewSchema.
    """
    return {
        "id": rotinapadrao.id,
        "hora": rotinapadrao.hora,
        "diasemana": rotinapadrao.diasemana,
        "evento": rotinapadrao.eventoAux.nome
    }    


def apresenta_rotinaspadrao(rotinaspadrao: List[RotinaPadrao]):
    """ Retorna uma representação de rotinas padrão seguindo o schema definido em
        RotinaPadraoViewSchema.
    """
    result = []
    for rotinapadrao in rotinaspadrao:
        result.append({
            "id": rotinapadrao.id,
            "hora": rotinapadrao.hora,
            "diasemana": rotinapadrao.diasemana,
            "evento": rotinapadrao.evento.nome,
            "id_evento": rotinapadrao.id_evento,
            "id_pessoa": rotinapadrao.id_pessoa
        })

    return {"rotinaspadrao": result}