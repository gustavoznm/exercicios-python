#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades
# de latas de tinta a serem compradas e o preço total.

import math
capacidadelata = 18
precotinta = 80
coberturatinta = 3

metros = float(input('Digite quantos metros quadrados você precisa pintar: '))

litros = (metros / coberturatinta)
latastinda = float(litros/capacidadelata)

if litros % capacidadelata != 0:

    litrostotal = math.ceil(latastinda)
    valortotal = litrostotal * precotinta
    print(f'Você ira precisa de {litrostotal} litros e custará R${valortotal:.2f}')
else:
    litrostotal = latastinda
    valortotal = litrostotal * precotinta
    print(f'Voce ira precisar de {litrostotal} litros e custará R${valortotal:.2f}')



