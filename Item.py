from TipoItem import TipoItem

class Item:
    def __init__(self, nome: str, descricao: str, tipo: TipoItem, valorEfeito: float):
        self.__nome = nome 
        self.__descricao = descricao 
        self.__tipo = tipo 
        self.__valorEfeito = valorEfeito

    @property
    def nome(self):
        return self.__nome
    @property
    def descricao(self):
        return self.__descricao
    @property
    def tipo(self):
        return self.__tipo
    @property
    def valorEfeito(self):
        return self.__valorEfeito
    
    def __str__(self):
        return f"{self.__nome} [{self.__tipo.value}] - Efeito: {self.__valorEfeito}"