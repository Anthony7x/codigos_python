soma = 0 #estamos inicializando a variável com o valor zero
total_pares = 0 #será responsável por contar todos os valores pares

for contador in range(50,71):
    if contador % 2 == 0:
        soma = soma + contador #soma += contador
        total_pares = total_pares + 1

print(f"A soma dos valores pares é {soma}, a média dos pares é {soma/total_pares}, onde o total de valores é {total_pares}")        