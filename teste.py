from personagem import Personagem
from missao import Missao, MissaoCombate, MissaoColeta, MissaoExploracao

personagem1 = Personagem("Bentley")

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

#SUCESSO
personagem1.concluir_missao(combate, 1)

#FRACASSO
personagem1.concluir_missao(coleta, 2)

personagem1.concluir_missao(exploracao, 15)

personagem1.exibir_dados()