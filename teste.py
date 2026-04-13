from personagem import Personagem
from missao import Missao, MissaoCombate, MissaoColeta, MissaoExploracao

personagem1 = Personagem("Bentley")
personagem2 = Personagem("Sly")

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
    2
)


print(combate)
combate.iniciar_missao()
combate.concluir_missao(1)
combate.exibir_dados()

print(coleta)
coleta.iniciar_missao()
coleta.concluir_missao(10)
coleta.exibir_dados()

print(exploracao)
exploracao.iniciar_missao()
exploracao.concluir_missao(20)
exploracao.exibir_dados()