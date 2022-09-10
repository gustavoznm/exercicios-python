#Faça um Programa que pergunte quanto você ganha por hora e o número
# de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horas = int(input('Digite quantas horas você trabalhou no mes: '))
valorhr = float(input('Digite quanto você ganha por hora: '))

salario = horas * valorhr

print(f'O seu salario no final do mês sera de: R${salario:.0f},00')