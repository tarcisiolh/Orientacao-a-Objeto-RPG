class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.__nivel = 1
        self.__xp = 0
        self.__vida = 100

    @property
    def nome(self):
        return self.__nome

    @property
    def nivel(self):
        return self.__nivel

    @property
    def xp(self):
        return self.__xp

    @property
    def vida(self):
        return self.__vida

    @nome.setter
    def nome(self, novoNome: str):
        if not novoNome or not novoNome.strip():
            raise Exception("Nome é obrigatório.")
        self.__nome = novoNome.strip()

    def __str__(self):
        return f"PERSONAGEM:\nNome: {self.nome}\nNível: {self.nivel}\nXP: {self.xp}\nVida: {self.vida}\n"

    def __eq__(self, other):
        if not isinstance(other, Personagem):
            return False
        return self.nome == other.nome

    def exibir_dados(self):
        print(self.__str__())