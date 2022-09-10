import random
from random import randint
computador = randint(0, 10)
print('Prazer Humano, sou seu computador... Acabei de pensar em um número entre 0 e 10. ')
print('Vamos brincar? Sera que você consegue adivinhar o número em que pensei? ')
acertou = False
cont = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    cont += 1
    print(computador)
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez! ')
        else:
            print('Menos.. Tente mais uma vez! ')

print(f'Foram necessarias {cont} tentativas para o computador acertar o número. ')



