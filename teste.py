from personagem import Personagem
from missao import MissaoCombate, MissaoColeta, MissaoExploracao
from Item import Item
from TipoItem import TipoItem

personagem1 = Personagem("Bentley", vidaBase=80, ataqueBase=15.0) 

bengala_mecanica = Item("Bengala Mecânica", "Aumenta o ataque corpo a corpo", TipoItem.ARMA, 25.0)
armadura_casco = Item("Armadura de Casco", "Aumenta a vida total", TipoItem.VESTIMENTA, 10.0) 
oculos_binocucom = Item("Binocucom de Alta Tecnologia", "Aumenta a resistência e vida", TipoItem.UTILITARIO, 5.0) 

personagem1.add_item(bengala_mecanica)
personagem1.add_item(armadura_casco)
personagem1.add_item(oculos_binocucom)

personagem1.mostrar_inventario()

personagem1.equiparItens(arma=bengala_mecanica, vestimenta=armadura_casco, utilitario=oculos_binocucom)

combate = MissaoCombate(
    "Printing Press Duel",
    "Derrote Dimitri e reivindique as penas do Clockwerk",
    40,
    "Iguana",
    1
)

coleta = MissaoColeta(
    "Ghost Capture",
    "Liberte os fantasmas e os capture com seu binocucom",
    20,
    "Fantasma",
    5
)

exploracao = MissaoExploracao(
    "Recon the Ballroom",
    "Entre no salão e tire as fotos necessárias de reconhecimento",
    30,
    "Ballroom",
    10
)

personagem1.add_missao(combate)
personagem1.add_missao(coleta)
personagem1.add_missao(exploracao)

# SUCESSO
personagem1.concluir_missao(combate, 1)

# FRACASSO
personagem1.concluir_missao(coleta, 2)

# SUCESSO
personagem1.concluir_missao(exploracao, 15)

personagem1.exibir_dados()