from personagem import Personagem
from missao import MissaoCombate, MissaoColeta, MissaoExploracao
from Status import EstadoAndamento
from Item import Item
from TipoItem import TipoItem

def main():
    jogador = Personagem("Sly", vidaBase=100, ataqueBase=20.0)
    
    while True:
        print(f"\n=== MENU RPG - {jogador.nome} ===")
        print("1. Ver Atributos do Personagem")
        print("2. Adicionar Missão")
        print("3. Concluir Missão")
        print("4. Listar Missões em Andamento")
        print("5. Ver Inventário")
        print("6. Adicionar Item")
        print("7. Equipar Item")
        print("8. Sair")
        
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
                    item_nec = input("Item necessário: ")
                    qtd = int(input("Quantidade: "))
                    missao = MissaoColeta(nome, desc, recompensa, item_nec, qtd)
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
            jogador.mostrar_inventario()
            
        elif opcao == "6":
            print("\nTipos de Item:")
            print("1. Arma")
            print("2. Vestimenta")
            print("3. Utilitário")
            tipo_escolha = input("Escolha o tipo: ")
            
            nome_item = input("Nome do Item: ")
            desc_item = input("Descrição: ")
            valor_efeito = float(input("Valor do Efeito (Bônus): "))
            
            try:
                if tipo_escolha == "1":
                    novo_item = Item(nome_item, desc_item, TipoItem.ARMA, valor_efeito)
                elif tipo_escolha == "2":
                    novo_item = Item(nome_item, desc_item, TipoItem.VESTIMENTA, valor_efeito)
                elif tipo_escolha == "3":
                    novo_item = Item(nome_item, desc_item, TipoItem.UTILITARIO, valor_efeito)
                else:
                    print("Opção inválida.")
                    continue
                    
                jogador.add_item(novo_item)
            except Exception as e:
                print(f"Erro ao adicionar item: {e}")
                
        elif opcao == "7":
            jogador.mostrar_inventario()
            nome_equip = input("Digite o nome EXATO do item que deseja equipar: ")
            
            item_encontrado = None
            for item in jogador._Personagem__inventario:
                if item.nome == nome_equip:
                    item_encontrado = item
                    break
                    
            if not item_encontrado:
                print("Item não encontrado no inventário.")
            else:
                if item_encontrado.tipo == TipoItem.ARMA:
                    jogador.equiparItens(arma=item_encontrado)
                elif item_encontrado.tipo == TipoItem.VESTIMENTA:
                    jogador.equiparItens(vestimenta=item_encontrado)
                elif item_encontrado.tipo == TipoItem.UTILITARIO:
                    jogador.equiparItens(utilitario=item_encontrado)
                
        elif opcao == "8":
            print("Saindo do RPG...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()