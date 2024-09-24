import random

def jogar_moeda():
    return random.choice(["Cara", "Coroa"])

def executar_simulador():
    resultados_lancamentos = []
    while True:
        resultado_moeda = jogar_moeda()
        print(f"Resultado: {resultado_moeda}")
        resultados_lancamentos.append(resultado_moeda)

        continuar = input("Deseja lançar novamente? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    print("Resultados acumulados:", resultados_lancamentos)

executar_simulador()
