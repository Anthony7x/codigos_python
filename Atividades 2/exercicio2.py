nome = input("Informe seu nome: ")
sexo = input("Informe seu gênero,(F)eminino e (M)asculino: ")
estado = input("Informe seu estado civil, solteiro(a), casado(a): ")

if sexo == "F" and estado == "casado(a)":
    tempoCasada = input("Quanto de casado(a): ")
    print(f"{nome}, você está casada há {tempoCasada} anos.")
else:
    print(f"{nome}, obrigado e até a próxima")    



