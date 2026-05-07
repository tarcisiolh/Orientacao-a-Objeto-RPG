from TipoItem import TipoItem

class Item:
    def __init__(self, nome: str, descricao: str, tipo: TipoItem, valorEfeito: float):
        self.nome = nome 
        self.descricao = descricao 
        self.tipo = tipo 
        self.valorEfeito = valorEfeito

    def __str__(self):
        return f"{self.nome} [{self.tipo.value}] - Efeito: {self.valorEfeito}"