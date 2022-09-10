print('=' * 25)
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
#formula progresao aritimetica an = a1 + (n-1). r

resultado = primeiroTermo + (10-1) * razao

for c in range(primeiroTermo, resultado+1, razao):
    print(f'{c}', end= ' -> ')
print('Acabou')
print('=' * 25)