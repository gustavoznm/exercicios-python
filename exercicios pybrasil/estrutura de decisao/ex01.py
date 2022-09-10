#Faça um Programa que peça dois números e imprima o maior deles.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

if numero1 > numero2:
    maior = numero1
    print(f'O número {maior} é o maior!')
else:
    maior = numero2
    print(f'O número {numero2} é o maior! ')