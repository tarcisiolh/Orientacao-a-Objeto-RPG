from Status import EstadoPendente

class Missao:
    def __init__(self, nome:str, descricao:str, recompensa:int):
        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa
        self.estado = EstadoPendente(self)

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def recompensa(self):
        return self.__recompensa

    @nome.setter
    def nome(self, novoNome: str):
        if not novoNome or not novoNome.strip():
            raise Exception("Nome é obrigatório.")
        self.__nome = novoNome.strip()

    @descricao.setter
    def descricao(self, novaDesc: str):
        if not novaDesc or not novaDesc.strip():
            raise Exception("Descrição é obrigatória.")
        self.__descricao = novaDesc.strip()

    @recompensa.setter
    def recompensa(self, novaRecomp: int):
        if novaRecomp < 1 or novaRecomp > 50:
            raise Exception("Recompensa deve estar entre 1 e 50.")
        self.__recompensa = novaRecomp

    def __str__(self):
        return f"MISSÃO:\nNome: {self.nome}\nDescrição: {self.descricao}\nRecompensa: {self.recompensa}\nStatus: {self.estado.nome}\n"

    def __eq__(self, other):
        if not isinstance(other, Missao):
            return False
        return self.nome == other.nome and self.descricao == other.descricao

    def exibir_dados(self):
        print(f"MISSÃO:\nNome: {self.nome}\nDescrição: {self.descricao}\nRecompensa: {self.recompensa}\nStatus: {self.estado.nome}\n")
        
    def iniciar_missao(self):
        self.estado.iniciar()

    def concluir_missao(self, valor):
        return self.estado.concluir(valor)

    def verificar_sucesso(self, valor):
        raise NotImplementedError("Método deve ser implementado pelas subclasses")


class MissaoCombate(Missao):
    def __init__(self, nome, descricao, recompensa, tipo_inimigo: str, inimigos_a_derrotar: int):
        super().__init__(nome, descricao, recompensa)
        self.tipo_inimigo = tipo_inimigo
        self.inimigos_a_derrotar = inimigos_a_derrotar

    @property
    def tipo_inimigo(self):
        return self.__tipo_inimigo
    
    @property
    def inimigos_a_derrotar(self):
        return self.__inimigos_a_derrotar
    
    @tipo_inimigo.setter
    def tipo_inimigo(self, novoTipIn: str):
        if not novoTipIn or not novoTipIn.strip():
            raise Exception("Tipo de inimigo é obrigatório.")
        self.__tipo_inimigo = novoTipIn.strip()

    @inimigos_a_derrotar.setter
    def inimigos_a_derrotar(self, quantidade: int):
        if quantidade <= 0:
            raise Exception("Quantidade de inimigos deve ser maior que zero.")
        self.__inimigos_a_derrotar = quantidade

    def __str__(self):
        base = super().__str__()
        return base + f"Tipo de inimigo: {self.tipo_inimigo}\nInimigos a derrotar: {self.inimigos_a_derrotar}\n"
    
    def verificar_sucesso(self, valor):
        return valor >= self.inimigos_a_derrotar
    

class MissaoColeta(Missao):
    def __init__(self, nome, descricao, recompensa, item_necessario: str, quantidade_item: int):
        super().__init__(nome, descricao, recompensa)
        self.item_necessario = item_necessario
        self.quantidade_item = quantidade_item

    @property
    def item_necessario(self):
        return self.__item_necessario

    @property
    def quantidade_item(self):
        return self.__quantidade_item

    @item_necessario.setter
    def item_necessario(self, novoItem: str):
        if not novoItem or not novoItem.strip():
            raise Exception("Item necessário é obrigatório.")
        self.__item_necessario = novoItem.strip()

    @quantidade_item.setter
    def quantidade_item(self, quantidade: int):
        if quantidade <= 0:
            raise Exception("Quantidade deve ser maior que zero.")
        self.__quantidade_item = quantidade

    def __str__(self):
        base = super().__str__()
        return base + f"Item necessário: {self.item_necessario}\nQuantidade: {self.quantidade_item}\n"

    def verificar_sucesso(self, valor):
        return valor >= self.quantidade_item


class MissaoExploracao(Missao):
    def __init__(self, nome, descricao, recompensa, regiao_destino: str, distancia_em_km: float):
        super().__init__(nome, descricao, recompensa)
        self.regiao_destino = regiao_destino
        self.distancia_em_km = distancia_em_km

    @property
    def regiao_destino(self):
        return self.__regiao_destino

    @property
    def distancia_em_km(self):
        return self.__distancia_em_km

    @regiao_destino.setter
    def regiao_destino(self, novaRegiao: str):
        if not novaRegiao or not novaRegiao.strip():
            raise Exception("Região de destino é obrigatória.")
        self.__regiao_destino = novaRegiao.strip()

    @distancia_em_km.setter
    def distancia_em_km(self, distancia: float):
        if distancia <= 0:
            raise Exception("Distância deve ser maior que zero.")
        self.__distancia_em_km = distancia

    def __str__(self):
        base = super().__str__()
        return base + f"Região destino: {self.regiao_destino}\nDistância: {self.distancia_em_km} km\n"

    def verificar_sucesso(self, valor):
        return valor >= self.distancia_em_km