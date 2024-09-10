#Faça um programa que recebe a quantidade de horas trabalhadas e o valor por hora de um funcionário. Se o número de horas for superior a 40, o funcionário receberá um bônus de 50% sobre as horas extras.

horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora: "))

horas_normais = 40

if horasTrabalhadas > horas_normais:
    horas_extras = horasTrabalhadas - horas_normais
    pagamento_normal = horas_normais * valor_por_hora
    pagamento_extras = horas_extras * valor_por_hora * 1.5
    salario_total = pagamento_normal + pagamento_extras
else:
    salario_total = horasTrabalhadas * valor_por_hora

print(f"O salário total é: R$ {salario_total:.2f}")



