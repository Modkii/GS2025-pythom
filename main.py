
from chamados import GerenciadorChamados
from alocacao import melhor_alocacao
from grafo import grafo, dijkstra, mostrar_rota


def main():
    chamados = GerenciadorChamados()

    contador_id = max([c['id'] for c in chamados.listar()], default=0) + 1

    while True:
        print("\n=== Sistema de Controle de Incêndios ===")
        print("1. Inserir chamado")
        print("2. Atender próximo chamado")
        print("3. Listar fila de chamados")
        print("4. Calcular melhor alocação")
        print("5. Calcular rota pelo grafo (Base → Destino)")
        print("6. Deletar chamado por ID")
        print("7. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':

            regiao = input("Região (ex.: Norte, Sul, Leste, Oeste): ")

            # Validação da gravidade (1 a 10)
            while True:
                try:
                    gravidade = int(input("Gravidade (1 a 10): "))
                    if 1 <= gravidade <= 10:
                        break
                    else:
                        print("Gravidade inválida. Digite um valor entre 1 e 10.")
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro entre 1 e 10.")

            # Validação da distância (em km, precisa ser maior que zero)
            while True:
                try:
                    distancia = float(input("Distância até a região (em km): "))
                    if distancia > 0:
                        break
                    else:
                        print("A distância precisa ser maior que zero.")
                except ValueError:
                    print("Entrada inválida. Digite um número válido.")

            chamado = {
                'id': contador_id,
                'regiao': regiao,
                'gravidade': gravidade,
                'distancia': distancia
            }

            contador_id += 1

            chamados.adicionar(chamado)

            print("\nChamado inserido com sucesso.")
            input("\nAperte ENTER para voltar ao menu...")

        elif opcao == '2':
            chamado = chamados.proximo()

            if chamado:
                print(f"\nAtendendo chamado: {chamado}")
            else:
                print("\nNenhum chamado na fila.")

            input("\nAperte ENTER para voltar ao menu...")

        elif opcao == '3':
            fila = chamados.listar()

            if fila:
                print("\n=== Fila de Chamados ===")
                for c in fila:
                    print(c)
            else:
                print("\nFila vazia.")

            input("\nAperte ENTER para voltar ao menu...")

        elif opcao == '4':
            focos = chamados.listar()

            if not focos:
                print("\nSem chamados na fila.")
            else:
                try:
                    n_cam = int(input("Quantos caminhões disponíveis? "))

                    selecionados, soma_grav, soma_score = melhor_alocacao(focos, n_cam)

                    print("\n=== Alocação Ideal ===")
                    for c in selecionados:
                        print(f"ID: {c['id']} | Região: {c['regiao']} | Gravidade: {c['gravidade']} | Distância: {c['distancia']} km | Score: {c['score']:.2f}")

                    print(f"\nGravidade total atendida: {soma_grav}")
                    print(f"Pontuação total: {soma_score:.2f}")

                except ValueError:
                    print("\nEntrada inválida.")

            input("\nAperte ENTER para voltar ao menu...")

        elif opcao == '5':
            destino = input("Destino: ").capitalize()

            origem = "Base"

            custo, caminho = dijkstra(grafo, origem, destino)

            if caminho and custo != float('inf'):
                mostrar_rota(grafo, caminho, custo)
            else:
                print("\nRota impossível. Verifique se o destino existe no grafo.")

            input("\nAperte ENTER para voltar ao menu...")

        elif opcao == '6':
            try:
                id_deletar = int(input("Digite o ID do chamado para deletar: "))

                sucesso = chamados.deletar(id_deletar)

                if sucesso:
                    print("\nChamado deletado com sucesso.")
                else:
                    print("\nChamado não encontrado.")

            except ValueError:
                print("\nID inválido.")

            input("\nAperte ENTER para voltar ao menu...")

        elif opcao == '7':
            print("\nEncerrando sistema...")
            break

        else:
            print("\nOpção inválida.")
            input("\nAperte ENTER para voltar ao menu...")


if __name__ == "__main__":
    main()
