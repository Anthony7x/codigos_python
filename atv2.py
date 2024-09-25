def mostrarMoedas(cotacoes):
    print("Moedas disponíveis:")
    for moeda, preco in cotacoes.items():
        print(f"{moeda}: R$ {preco:.2f}")

def converMoeda(cotacoes):
    while True:
        mostrarMoedas(cotacoes)
        moeda = input("Digite a moeda para conversão (ou 'sair' para encerrar): ").strip().lower()
        
        if moeda == 'sair':
            break
        elif moeda in cotacoes:
            valor_reais = float(input("Digite o valor em reais: "))
            valor_convertido = valor_reais / cotacoes[moeda]
            print(f"Valor convertido: {valor_convertido:.2f} {moeda.upper()}")
        else:
            print("Moeda não encontrada.")

def menu_moedas():
    cotacoes = {
        'dólar': 5.48,
        'euro': 6.10,
        'libra': 7.30,
        'iene': 0.038,
        'franco suíço': 6.44
    }
    converMoeda(cotacoes)

menu_moedas()
