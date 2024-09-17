'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, 
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )'''

meses = ['Janeiro',
        'Fevereiro', 
        'Março', 
        'Abril', 
        'Maio', 
        'Junho', 
        'Julho', 
        'Agosto', 
        'Setembro', 
        'Outubro', 
        'Novembro', 
        'Dezembro']

temperaturas = []

for cont in range(12):
    temp = float(input(f"Digite a temperatura média do mês {cont+1}: "))
    temperaturas.append(temp)

print("="*50)

somaTemp = 0
for temp in temperaturas:
    somaTemp += temp

mediaAnual = somaTemp / 12

print(f"A média anual das temperaturas é: {mediaAnual:.2f}°C")
print("="*50)
print("Meses com as temperaturas acima da média anual: ")

for cont in range(12):
    if temperaturas[cont] > mediaAnual:
        print(f"{meses[cont]} - {temperaturas[cont]}°C")
print("="*50)