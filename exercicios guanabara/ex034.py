salario = float(input('Digite o seu salário: '))

if salario <= 1250:

    salreaj = salario * 1.15
else:
    salreaj = salario * 1.10


print(f'Seu salario reajustado sera de: {salreaj:.2f}')