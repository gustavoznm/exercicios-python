import random
escolhido = float(input('Digite um número de 0 a 5: '))
numsorte = (0, 1, 2, 3, 4, 5)
sorteado = random.choice(numsorte)

print(f'O numero sorteado foi: {sorteado}')
if escolhido == sorteado:
    print('Você acertou o número! Parabéns')
else:
    print(f'Infelizmente você escolheu {escolhido} e o número que saiu foi o {sorteado}.')