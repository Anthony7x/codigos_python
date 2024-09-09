#Calcular a soma do valor inicial e final, mais os números em seu intervalo

N_inicial = int(input("Digite um valor: "))
N_final = int(input("Digite um valor: "))
soma = 0

for intervalo in range(N_inicial, N_final + 1):
    soma = soma + intervalo
print(f"A soma dos valores é {soma}")