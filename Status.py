from abc import ABC, abstractmethod

class EstadoMissao(ABC):
    def __init__(self, missao):
        self.missao = missao

    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def concluir(self, valor):
        pass

    @property
    @abstractmethod
    def nome(self):
        pass

class EstadoPendente(EstadoMissao):
    @property
    def nome(self):
        return "PENDENTE"

    def iniciar(self):
        self.missao.estado = EstadoAndamento(self.missao)
        print(f"A missão {self.missao.nome} começou! Objetivo central da missão: {self.missao.descricao}\n")

    def concluir(self, valor):
        raise Exception("O status da missão deve estar em andamento!")

class EstadoAndamento(EstadoMissao):
    @property
    def nome(self):
        return "EM ANDAMENTO"

    def iniciar(self):
        raise Exception("A missão já está em andamento!")

    def concluir(self, valor):
        if self.missao.verificar_sucesso(valor):
            self.missao.estado = EstadoConcluida(self.missao)
            return f"Missão concluída com sucesso. A contabilidade do prêmio de {self.missao.recompensa} XP agora está pronta para retirada financeira\n"
        else:
            self.missao.estado = EstadoFracassada(self.missao)
            return f"A missão {self.missao.nome} foi fracassada.\n"

class EstadoConcluida(EstadoMissao):
    @property
    def nome(self):
        return "CONCLUIDA"

    def iniciar(self):
        raise Exception("Missão já concluída.")

    def concluir(self, valor):
        raise Exception("Missão já concluída.")

class EstadoFracassada(EstadoMissao):
    @property
    def nome(self):
        return "FRACASSADA"

    def iniciar(self):
        raise Exception("Missão já fracassada.")

    def concluir(self, valor):
        raise Exception("Missão já fracassada.")