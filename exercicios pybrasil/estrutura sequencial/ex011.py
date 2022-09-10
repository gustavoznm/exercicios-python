#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#A) o produto do dobro do primeiro com metade do segundo .
#B) a soma do triplo do primeiro com o terceiro.
#C) o terceiro elevado ao cubo.

primeironum = int(input('Digite um numero inteiro: '))
segundonum = int(input('Digite outro numero inteiro: '))
terceironum = float(input('Digite um numero real: '))

a = (primeironum * 2) * (segundonum / 2)
b = (primeironum * 3) + terceironum
c = (terceironum  ** 3)

print(f'A) {a:.0F} ')
print(f'B) {b:.0F}')
print((f'C {c:.0F}'))