#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

print('O que você deseja fazer com esses valores? ')
operacao = int(input('Digite [1] - Somar\n'
                     'Digite [2] - Multiplicar \n'
                     'Digite [3] - Qual o maior \n'
                     'Digite [4] - Novos números \n'
                     'Digite [5] - Para sair do programa\n'
                     'Escolha sua opção: '))
soma = valor1 + valor2
multiplicacao = valor1 * valor2

if operacao == 1:
    print(f'A soma de {valor1} com {valor2} é {soma}')
elif operacao == 2:
    print(f'A multiplicação de {valor1} com {valor2} deu {multiplicacao}')
elif operacao == 3:
    if valor1 > valor2:
        maior = valor1
        print(f'O maior valor é {maior}')
    else:
        maior = valor2
        print(f'O maior valor é {maior}')
elif operacao == 4:
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    print('OPÇÃO NUMERO 4 COM PROBLEMAS KKK, VLW FLW')
else:
    print('=' * 10, 'VOCÊ ESCOLHEU SAIR DO PROGRAMA', '=' * 10 )
    print('Até mais!')



