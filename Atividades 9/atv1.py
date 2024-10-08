def addPrato(cardapio):
    prato = input("Digite o nome do prato: ")
    preco = float(input("Digite o preço do prato: "))
    cardapio[prato] = preco
    print(f"Prato '{prato}' foi adicionado ao cardápio com sucesso!")

def delPrato(cardapio):
    prato = input("Digite o nome do prato a ser removido: ")
    if prato in cardapio:
        del cardapio[prato]
        print(f"Prato '{prato}' removido com sucesso!")
    else:
        print("Prato não encontrado.")

def consultar_preco(cardapio):
    prato = input("Digite o nome do prato que deseja consultar: ")
    if prato in cardapio:
        print(f"O preço do prato '{prato}' é R$ {cardapio[prato]:.2f}")
    else:
        print("Prato não encontrado.")

def exibir_cardapio(cardapio):
    if cardapio:
        print("Cardápio:")
        for prato, preco in cardapio.items():
            print(f"{prato}: R$ {preco:.2f}")
    else:
        print("O cardápio está vazio.")

def menu_cardapio():
    cardapio = {}
    while True:
        print("="*50)
        print("\nEscolha uma opção:")
        print("="*50)
        print("1 - Adicionar prato")
        print("2 - Remover prato")
        print("3 - Consultar preço de um prato")
        print("4 - Exibir cardápio completo")
        print("="*50)
        print("5 - Sair")
        print("="*50)
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            addPrato(cardapio)
        elif opcao == '2':
            delPrato(cardapio)
        elif opcao == '3':
            consultar_preco(cardapio)
        elif opcao == '4':
            exibir_cardapio(cardapio)
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_cardapio()
