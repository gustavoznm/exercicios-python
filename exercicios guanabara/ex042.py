lado1 = float(input('Digite o primeiro segmento: '))
lado2 = float(input('Digite o segundo segmento: '))
lado3 = float(input('Digite o terceiro segmento: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Não é um triangulo! ')
elif lado1 == lado2 == lado3:
    print('Triangulo Equilatero! ')
elif lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado3 == lado1 != lado2:
    print('Triangulo Isoceles! ')
else:
    print('Triangulo Escaleno! ')





