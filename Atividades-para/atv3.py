#Faça um programa que receba a idade de 5 pessoas, calcule e mostre a quantidade de pessoas com idade maior igual a 18 anos.
maiores_de_idade = 0


for contador in range(5):
    idade = int(input(f"Digite a idade da {contador + 1} pessoa: "))

    if idade >= 18:
        maiores_de_idade += 1

print(f"A quantidade de pessoas que possuem 18 ou +18 é a seguinte: {maiores_de_idade}")        

