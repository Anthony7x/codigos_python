#1º forma de utilizar while - semelhante ao For
contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1 #é o mesmo que contador +=1
print("="*70)

#2º forma de utilizar - loop condicional normal
valor = 0

while valor >=0:
    valor = int(input("Informe um número qualquer (digite um valor negativo para terminar): "))
    print(f"Você digitou {valor}")

print("="*70)
#3º forma de utilizar o enquanto - semelhante a estrutura faça...enquanto

while True:
    senha = input("Digite sua senha: ")
    if senha == "123":
        print("Parabéns, senha correta")
        break #forma de encerrar o loop
    else:
        print("Senhas não conferem, tente novamente")