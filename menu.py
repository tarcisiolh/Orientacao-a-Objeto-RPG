from personagem import Personagem
from missao import MissaoCombate, MissaoColeta, MissaoExploracao
from Status import EstadoAndamento

def main():
    jogador = Personagem("Sly", vidaBase=100, ataqueBase=20.0)
    
    while True:
        print(f"\n=== MENU RPG - {jogador.nome} ===")
        print("1. Ver Atributos do Personagem")
        print("2. Adicionar Missão")
        print("3. Concluir Missão")
        print("4. Listar Missões em Andamento")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            jogador.exibir_dados()
            
        elif opcao == "2":
            print("\nTipos de Missão:")
            print("1. Combate")
            print("2. Coleta")
            print("3. Exploração")
            tipo = input("Escolha o tipo: ")
            
            nome = input("Nome da Missão: ")
            desc = input("Descrição: ")
            recompensa = int(input("Recompensa (XP): "))
            
            try:
                if tipo == "1":
                    tipo_inimigo = input("Tipo de Inimigo: ")
                    qtd = int(input("Quantidade a derrotar: "))
                    missao = MissaoCombate(nome, desc, recompensa, tipo_inimigo, qtd)
                elif tipo == "2":
                    item = input("Item necessário: ")
                    qtd = int(input("Quantidade: "))
                    missao = MissaoColeta(nome, desc, recompensa, item, qtd)
                elif tipo == "3":
                    regiao = input("Região: ")
                    dist = float(input("Distância (km): "))
                    missao = MissaoExploracao(nome, desc, recompensa, regiao, dist)
                else:
                    print("Opção inválida.")
                    continue
                    
                jogador.add_missao(missao)
            except Exception as e:
                print(f"Erro ao adicionar missão: {e}")
                
        elif opcao == "3":
            if not jogador.missoes:
                print("Nenhuma missão disponível.")
                continue
                
            print("\nSelecione a missão para concluir:")
            for i, m in enumerate(jogador.missoes):
                print(f"{i}. {m.nome} ({m.estado.nome})")
                
            idx = int(input("Índice da missão: "))
            valor = float(input("Digite o valor alcançado: "))
            
            try:
                missao_selecionada = jogador.missoes[idx]
                jogador.concluir_missao(missao_selecionada, valor)
            except Exception as e:
                print(f"Erro: {e}")
                
        elif opcao == "4":
            print("\n--- MISSÕES EM ANDAMENTO ---")
            andamento = [m for m in jogador.missoes if isinstance(m.estado, EstadoAndamento)]
            if not andamento:
                print("Nenhuma missão em andamento.")
            for m in andamento:
                print(f"- {m.nome} (Recompensa: {m.recompensa} XP)")
                
        elif opcao == "5":
            print("Saindo do RPG...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()