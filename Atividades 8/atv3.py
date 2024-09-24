import random

def misturar_palavras(lista_palavras):
    random.shuffle(lista_palavras)
    return lista_palavras

def iniciar_jogo(lista_opcoes):
    lista_misturada = misturar_palavras(lista_opcoes[:])  # Cópia da lista
    palavra_escolhida = random.choice(lista_misturada)
    posicao_correta = lista_misturada.index(palavra_escolhida)

    print(f"Tente adivinhar a posição da palavra '{palavra_escolhida}' na lista.")
    print("A lista vai de 0 a 14.")
    
    tentativas_restantes = 3
    while tentativas_restantes > 0:
        try:
            resposta_usuario = int(input("Digite a posição: "))
            if resposta_usuario == posicao_correta:
                print("Parabéns, você acertou!")
                break
            else:
                tentativas_restantes -= 1
                print(f"Erro! Tentativas restantes: {tentativas_restantes}")
        except ValueError:
            print("Insira um número válido.")
    
    if tentativas_restantes == 0:
        print(f"As tentativas acabaram! A palavra estava na posição {posicao_correta}.")
    
    print("Lista embaralhada:", lista_misturada)

def jogar_palavras():
    frutas = ['maçã', 'banana', 'laranja', 'morango', 'uva', 'abacaxi', 'kiwi', 'manga', 'pera', 'melancia',
              'framboesa', 'nectarina', 'carambola', 'figo', 'amora']
    iniciar_jogo(frutas)

jogar_palavras()