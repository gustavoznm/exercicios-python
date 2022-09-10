#Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.

tempf = float(input('Digite a temperatura em Fahhrenheit: '))

celc = (tempf - 32) / 1.8

print(f'A conversão de {tempf:.0f} Fahrenheit para Celcios é {celc:.0f}º !')