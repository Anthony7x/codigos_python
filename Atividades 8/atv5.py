def exibir_menu(eventos):
    print("\nMenu de Eventos")
    contador = 1
    for evento in eventos:
        print(f"{contador}. {evento}")
        contador += 1
    
    print("\n1. Adicionar um novo evento")
    print("2. Remover um evento")
    print("3. Sair")

def adicionar_evento(eventos):
    novo_evento = input("\nDigite o nome do novo evento: ")
    eventos.append(novo_evento)
    print(f"Evento '{novo_evento}' adicionado com sucesso.")

def remover_evento(eventos):
    if not eventos:
        print("Não há eventos para remover.")
        return
    
    posicao = input("\nQual a posição do evento a ser removido? ")
    
    if posicao.isnumeric():  # Verifica se a string contém apenas números
        posicao = int(posicao)
        if 1 <= posicao <= len(eventos):
            evento_removido = eventos.pop(posicao - 1)
            print(f"Evento '{evento_removido}' removido com sucesso.")
        else:
            print("Posição inválida.")
    else:
        print("Por favor, digite um número válido.")

def gerenciar_eventos():
    eventos = ["Ir para a escola."]
    
    while True:
        exibir_menu(eventos)
        
        opcao = input("\nEscolha uma opção (1-3): ")
        
        if opcao.isnumeric():  # Verifica se a string contém apenas números
            opcao = int(opcao)
            if opcao == 1:
                adicionar_evento(eventos)
            elif opcao == 2:
                remover_evento(eventos)
            elif opcao == 3:
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        else:
            print("Por favor, digite um número válido.")

gerenciar_eventos()