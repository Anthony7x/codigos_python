#OBS: "Tuplas = ()"
#Irei exibir o item na posição 1, ou seja segunda posição, uma vez que toda coleção começa na posição zero. 
objetos = ('Lápis','Borracha','Caderno')
print(objetos[1])

print(type(objetos)) #Irá mostrar o tipo da variável

print(objetos) #exibindo todos os itens de uma só vez

print('='*100)
for item in range(0,3):
    print(objetos[item]) #exibindo todos os itens da tupla

#exibindo todos os itens da tupla sem a função range
print('='*100)
for elementos in objetos:
    print(elementos) #exibindo todos os itens da tupla

#Iremos tentar alterar o contéudo da tupla
objetos[0] = "Caneta"    
    