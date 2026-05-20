from Item import Item
from TipoItem import TipoItem
from Status import EstadoConcluida, EstadoAndamento

class Personagem:
    def __init__(self, nome, vidaBase, ataqueBase):
        self.nome = nome
        self.__nivel = 1
        self.__xp = 0
        self.__vidaBase = vidaBase 
        self.__ataqueBase = ataqueBase
        self.__missoes = []
        
        self.__inventario = []
        self.__armaEquipada = None
        self.__vestimentaEquipada = None
        self.__utilitarioEquipada = None

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
        bonus_percentual = 0
        if self.__vestimentaEquipada:
            bonus_percentual += self.__vestimentaEquipada.valorEfeito 
        if self.__utilitarioEquipada:
            bonus_percentual += self.__utilitarioEquipada.valorEfeito 
        
        vida_calculada = self.__vidaBase * (1 + (bonus_percentual / 100.0))
        return min(100.0, vida_calculada) 

    @property
    def ataque(self):
        ataque_total = self.__ataqueBase
        if self.__armaEquipada:
            ataque_total += self.__armaEquipada.valorEfeito
        return ataque_total

    @property
    def missoes(self):
        return self.__missoes

    @nome.setter
    def nome(self, novoNome: str):
        if not novoNome or not novoNome.strip():
            raise Exception("Nome é obrigatório.")
        self.__nome = novoNome.strip()

    def add_item(self, item: Item):
        self.__inventario.append(item)
        print(f"Item '{item.nome}' adicionado ao inventário de {self.nome}.")

    def remover_item(self, item: Item):
        if item in self.__inventario:
            self.__inventario.remove(item)
            if self.__armaEquipada == item: self.__armaEquipada = None
            if self.__vestimentaEquipada == item: self.__vestimentaEquipada = None
            if self.__utilitarioEquipada == item: self.__utilitarioEquipada = None
            print(f"Item '{item.nome}' removido do inventário.")
        else:
            print("O item não está no inventário.")

    def mostrar_inventario(self):
        print(f"\n--- Inventário de {self.nome} ---")
        if not self.__inventario:
            print("Inventário vazio.")
        for item in self.__inventario:
            print(f"- {item}")
        print("------------------------------\n")

    def equiparItens(self, arma=None, vestimenta=None, utilitario=None):
        if arma:
            if arma in self.__inventario and arma.tipo == TipoItem.ARMA:
                self.__armaEquipada = arma
                print(f"{self.nome} equipou a Arma: {arma.nome}")
            else:
                print("Não foi possível equipar a arma (não encontrada ou tipo incorreto).")
                
        if vestimenta:
            if vestimenta in self.__inventario and vestimenta.tipo == TipoItem.VESTIMENTA:
                self.__vestimentaEquipada = vestimenta
                print(f"{self.nome} equipou a Vestimenta: {vestimenta.nome}")
            else:
                print("Não foi possível equipar a vestimenta (não encontrada ou tipo incorreto).")
                
        if utilitario:
            if utilitario in self.__inventario and utilitario.tipo == TipoItem.UTILITARIO:
                self.__utilitarioEquipada = utilitario
                print(f"{self.nome} equipou o Utilitário: {utilitario.nome}")
            else:
                print("Não foi possível equipar o utilitário (não encontrado ou tipo incorreto).")

    def __str__(self):
        missoes_str = "\n".join([f"- {m.nome} ({m.estado.nome})" for m in self.__missoes])
        return (
            f"PERSONAGEM:\n"
            f"Nome: {self.nome}\n"
            f"Nível: {self.nivel}\n"
            f"XP: {self.xp}\n"
            f"Ataque Total: {self.ataque}\n"
            f"Vida Total: {self.vida}\n"
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

        resultado = missao.concluir_missao(valor)
        print(resultado)

        if isinstance(missao.estado, EstadoConcluida):
            self.__xp += missao.recompensa
            print(f"{self.nome} ganhou {missao.recompensa} XP!\n")
        else:
            print(f"{self.nome} não ganhou XP nesta missão.\n")