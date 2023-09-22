from pydantic import BaseModel
from model.evento import Evento


class EventoSchema(BaseModel):
    """ Define como um evento deve ser representado.
    """
    id_pessoa: int = 1
    nome: str = "Almoço"


class EventoBuscaIdSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca pelo id.
    """
    id: int = 1   


class EventoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str    


def apresenta_evento(evento: Evento):
    """ Retorna uma representação do evento.
    """
    return {
        "id": evento.id,
        "nome": evento.nome
    }    