'''Faça um programa que leia um ano e determine se ele é bissexto. Um ano é
bissexto se:
a. For divisível por 400, ou
b. For divisível por 4, mas não divisível por 100.'''

ano = int(input("Digite um ano: "))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")
