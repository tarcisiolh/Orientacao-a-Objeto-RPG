class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.__nivel = 1
        self.__xp = 0
        self.__vida = 100
        self.__missoes = []

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
        missoes_str = "\n".join([f"- {m.nome} ({m.status.value})" for m in self.__missoes])
        return (
            f"PERSONAGEM:\n"
            f"Nome: {self.nome}\n"
            f"Nível: {self.nivel}\n"
            f"XP: {self.xp}\n"
            f"Vida: {self.vida}\n"
            f"Missões:\n{missoes_str if missoes_str else 'Nenhuma missão'}\n"
        )

    def __eq__(self, other):
        if not isinstance(other, Personagem):
            return False
        return self.nome == other.nome

    def exibir_dados(self):
        print(self.__str__())

    def add_missao(self, missao):
        if missao in self.__missoes:
            raise Exception("Missão já adicionada.")
        
        self.__missoes.append(missao)
        missao.iniciar_missao()
        print(f"Missão '{missao.nome}' adicionada ao personagem {self.nome}.\n")

    def concluir_missao(self, missao, valor):
        if missao not in self.__missoes:
            raise Exception("Missão não pertence a este personagem.")

        missao.concluir_missao(valor)


        if missao.status.value == "CONCLUIDA":
            self.__xp += missao.recompensa
            print(f"{self.nome} ganhou {missao.recompensa} XP!\n")
        else:
            print(f"{self.nome} não ganhou XP.\n")