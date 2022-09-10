#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celcius = float(input('Digite a temperatura em Graus Celcius: '))

tempf = (celcius * 1.8) + 32

print(f'A conversão de {celcius:.0f} para Fahrenheit é de {tempf:.0f} graus fahrenheit!')