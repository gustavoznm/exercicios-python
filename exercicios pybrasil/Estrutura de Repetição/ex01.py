#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
# e continue pedindo até que o usuário informe um valor válido.
nota = int(input('Digite uma nota entre 0 e 10: '))
notas = (0, 10)
while nota not in notas:
    nota = int(input('Valor invalido, tente novamente:  '))
print(f'A nota digitada foi {nota}')
