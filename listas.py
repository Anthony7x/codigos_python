#Listas = []
animais = ["Cachorro", "Gato","Ovelha"]
print(type(animais)) #exibindo o tipo de variável

print(animais)

#exibindo todos os itens da lista
print("="*100)
for items in animais:
    print(items)

#1ª Etapa: Atualizar dados
print("="*100)
animais[0] ="Coelho"
print(animais)   

#2ª Etapa: Inserir dados
print("="*100)

#Forma 1 - Usando append
animais.append("Cavalo")#Irá inserir um novo item no final da lista

#Forma 2 - Insert
animais.insert(1,"Leão") #O insert precisa de 2 valores, o 1ª será o índice que o desejo inserir o valor. O 2º é o conteúdo que quero inserir na lista.
print(animais)

#3ª Etapa: Excluir dados
print("="*100)

#Forma 1 - usando.pop()
print(animais.pop(1)) #O pop irá excluir o item que estiver
print(animais)

#Forma 2 - usando pop() com índice
animais.pop(0) #Aqui iremos escolher qual índice da lista será excluído.
print(animais)

#Forma 3 - Usando remove
animais.remove("Gato") #Irá remover o item pelo seu conteúdo
print(animais)