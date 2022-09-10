velocidade = float(input('Digite a velocidade em que o carro estava: '))
velacima = (velocidade - 80)
multa = (velacima * 7)

if velocidade > 80:
    print('Você foi multado!!')
    print(f'A sua multa sera no valor de R${multa},00 que é o equivalente a R$7,00 por KM passado da velocidade limite! ')
else:
    print(f'Você estava a {velocidade} km/hr, que é aceitavel nessa pista, está tudo certo, pode continuar viagem! ')