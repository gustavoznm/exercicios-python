#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
# são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
# e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
# (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o
# exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

horastrabalhadas = int(input('Digite quantas horas você trabalha por mês: '))
valorhora = float(input('Digite quanto você recebe por hora: '))

salariobruto = valorhora * horastrabalhadas

ir1500 = 0.05
ir2500 = 0.1
iracima2500 = 0.2
#fgts não desconta do salario, empresa deposita!
fgts = 0.11
sindicato = 0.03

descontofgts = salariobruto * fgts
if salariobruto <= 900:
    salarioliquido = (salariobruto - (salariobruto * sindicato))

elif salariobruto > 900 and salariobruto <= 1500:
    salarioliquido = (salariobruto - (salariobruto * ir1500) - ( salariobruto * sindicato))
    irvalor = salariobruto * ir1500
    fgtsvalor = salariobruto * fgts
    ir = ('5%')
elif salariobruto > 1500 and salariobruto <= 2500:
    salarioliquido = (salariobruto - (salariobruto * ir2500) - (salariobruto * sindicato))
    irvalor = salariobruto * ir2500
    fgtsvalor = salariobruto * fgts
    ir = ('10%')
else:
    salarioliquido = (salariobruto- (salariobruto * iracima2500) - (salariobruto * sindicato))
    irvalor = salariobruto * iracima2500
    fgtsvalor = salariobruto * fgts
    ir = ('20%')

print(f'Salário bruto        : R${salariobruto:.2f}')
print(f'(-) IR ({ir})          : R$ {irvalor}')


