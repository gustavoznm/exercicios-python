valorAserPago = float(input('Digite qual o valor a ser pago: R$'))
condicao = int(input('Digite qual forma de pagamento você quer pagar: \n'
      '[1] Á vista Dinheiro/Cheque \n'
      '[2] Á vista no cartão \n'
      '[3] Em 2x no cartão \n'
      '[4] 3x ou mais \n'))

aVista1 = valorAserPago * 0.9
aVista2 = valorAserPago * 0.95
duasVezes = valorAserPago
tresOuMais = valorAserPago * 1.20


if condicao == 1:
      print(f'Você ira pagar R${aVista1:.2f} com os 10% de desconto.')
elif condicao == 2:
      print(f'Você ira pagar R${aVista2:.2f} com os 5% de desconto. ')
elif condicao == 3:
      valorparcela = valorAserPago / 2
      print(f'Parcelando em 2x não terá descontos/juros e irá pagar R${duasVezes:.2f} e cada parcela ficará R${valorparcela:.2f}')
elif condicao == 4:
      numeroParcelas = int(input('Em quantas parcelas irá pagar? '))
      valorparcela = valorAserPago / numeroParcelas
      print(f'Você ira pagar R${tresOuMais:.2f}, irá ficar R${valorparcela} por mês durante {numeroParcelas} meses.')
else:
      print(f'Você selecionou uma opção invalida!  \n'
            f'Sua compra sera no valor de R${valorAserPago:.2f}')
