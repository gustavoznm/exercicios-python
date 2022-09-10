from random import choices

nome1 = input('Digite o primeiro nome! ')
nome2 = input('Digite o segundo nome!  ')
nome3 = input('Digite o terceiro nome! ')
nome4 = input('Digite o quarto nome! ')
nome5 = input('Digite o quinto nome! ')

alunoesco = [nome1, nome2, nome3, nome4, nome5]
sorteio = choices(alunoesco)

print(f'O aluno escolhido no sorteio foi {sorteio}')

`${sorteio}`

