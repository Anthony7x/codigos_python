import random

def gerar_numeros_aleatorios(inicio, fim):
    return random.randint(inicio, fim)

def menu_numeros_aleatorios():
    numeros_gerados = []
    for _ in range(5):
        inicio = int(input("Digite o limite inferior: "))
        fim = int(input("Digite o limite superior: "))
        numero = gerar_numeros_aleatorios(inicio, fim)
        numeros_gerados.append(numero)
        print(f"Número aleatório gerado: {numero}")
    print("Números gerados:", numeros_gerados)

menu_numeros_aleatorios()
