from pydantic import BaseModel
from typing import Optional, List
from model.pessoa import Pessoa

from schemas import EventoSchema


class PessoaSchema(BaseModel):
    """ Define como uma pessoa deve ser representada.
    """
    nome: str = "Petrus Fidelis"


class PessoaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da pessoa.
    """
    nome: str = "Pietro"


class PessoaBuscaIdSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca pelo id.
    """
    id: int = 1   


class ListagemPessoasSchema(BaseModel):
    """ Define como uma listagem de pessoas será retornada.
    """
    pessoas:List[PessoaSchema]


def apresenta_pessoas(pessoas: List[Pessoa]):
    """ Retorna uma representação da pessoas seguindo o schema definido em
        PessoaViewSchema.
    """
    result = []
    for pessoa in pessoas:
        result.append({
            "id": pessoa.id,
            "nome": pessoa.nome
        })

    return {"pessoas": result}


class PessoaViewSchema(BaseModel):
    """ Define como uma pessoa será retornada.
    """
    id: int = 1
    nome: str = "Petrus Fidelis",
    eventos:List[EventoSchema]


class PessoaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str


def apresenta_pessoa(pessoa: Pessoa):
    """ Retorna uma representação da pessoa.
    """
    return {
        "id": pessoa.id,
        "nome": pessoa.nome,
        "total_eventos": len(pessoa.eventos),
        "eventos": [{"id": c.id, "nome": c.nome} for c in pessoa.eventos]
    }
