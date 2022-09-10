numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero+1 ):
    if numero % c == 0:
        print('\033[033m', end='')
        total += 1
    else:
        print('\033[031m', end='')

    print(f'{c} ', end='')
print(f'\nO número {numero} foi divisivel {total} vezes')
if total == 2:
    print('Ele é um número primo!')
else:
    print('Não é um número primo! ')