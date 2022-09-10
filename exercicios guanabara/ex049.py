numero = int(input('Digite um número que deseja ver a tabuada: '))

for c in range(0, 10):
    resultado = numero * c
    c += 1
    print(f' {numero} x {c} = {resultado}')



