nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) /2
print(f' Tirando as notas {nota1} e {nota2} sua média ficou {media}')
if media < 5:
    print('O aluno esta Reprovado! ')
elif media >= 5 and media < 7:
    print('O aluno esta em recuperação! ')
elif media >= 7:
    print('O aluno esta Aprovado! ')

