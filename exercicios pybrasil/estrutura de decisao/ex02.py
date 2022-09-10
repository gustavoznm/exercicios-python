#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input('Digite um valor: '))

if valor > 0:
    print(f'O valor que digitou, {valor:.0f} é positivo! ')
else:
    print(f'O valor que digitou, {valor:.0f} é negativo')