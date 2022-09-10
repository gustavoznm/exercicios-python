#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math
coberturatinta = 6
capacidadelata = 18
precolata = 80
capacidadegalao = 3.6
precogalao = 25

metros = int(input('Digite a quantidade em metros quadrados da área que precisa pintar: '))

areacomfolga  = metros * 1.1
litros = areacomfolga / coberturatinta
latastinta = float(math.ceil(litros/capacidadelata))
valorlata = latastinta * precolata
galaotinta = float(math.ceil(litros/capacidadegalao))
valorgalao = galaotinta * precogalao

print(f'Você devera usar {latastinta} latas de 18 litros, no valor de R${valorlata:.2f}')

print(f'Você devera usar {galaotinta} galões de 3.6 litros, no valor de R${valorgalao:.2f} ')

#compra de tinta otimizada por valor!

latastinta = float(math.floor(litros/capacidadelata))
valordelatas = latastinta * 80
litros_faltantes = litros % capacidadelata
galaotinta = float(math.ceil(litros_faltantes/capacidadegalao))
valorcomgalao = galaotinta * precogalao

valor_total = valordelatas + valorcomgalao

print(f'Você devera usar {latastinta} em latas de 18 litros + {galaotinta} galões de tinta, no valor de: {valor_total}')






