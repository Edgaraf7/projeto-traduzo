# src/models/language_model.py

from .abstract_model import AbstractModel
from ..database.db import languages_collection


class LanguageModel(AbstractModel):
    # Definindo a coleção "languages"
    _collection = languages_collection

    def __init__(self, data):
        # Chamando o construtor da classe pai com os dados recebidos
        super().__init__(data)

    def to_dict(self):
        """
        Converte os atributos do objeto em um dicionário.
        """
        return {
            "name": self.data.get("name"),
            "acronym": self.data.get("acronym")
        }

    @classmethod
    def list_dicts(cls):
        """
        Lista todos os dicionários dos idiomas presentes na coleção,
        apenas com os campos 'name' e 'acronym'.
        """
        languages = cls._collection.find()
        return [{"name": language["name"], "acronym":
                 language["acronym"]} for language in languages]
