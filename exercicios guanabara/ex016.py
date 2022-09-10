diasalug = int(input('Digite quantos dias você ficou com o carro alugado! '))
quantkm = float(input('Digite a quantidade de KM rodados com o carro! '))
precodia = 60 * diasalug
precokm = 0.15 * quantkm
precototal = precokm + precodia

print(f'''Você irá pagar um total de R$ {precototal:.2f} 
por ter alugado o carro por {diasalug} dias e rodado {quantkm:.0f} KM com o carro! ''')

