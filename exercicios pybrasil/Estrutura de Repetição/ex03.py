#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = str(input('Digite seu nome [MINIMO 4 CARACTERES]:  '))
idade = int(input('Digite sua idade: '))

idadeentre = (0, 150)
while len(nome) <= 3:
    nome = str(input('Nome invalido, contem menos de 3 letras... Digite novamente! '))
print(f'Seu nome é {nome}')

while (idade < 0 or idade > 150):
    idade = int(input('Idade invalida, digite novamente: '))
print(f'Sua idade é de {idade} anos')
salario = float(input('Digite seu salario : R$'))
while salario == 0:
    salario = float(input('Salário invalido, digite seu salário novamente: '))
print(f' Seu salário é de R${salario:.2f} ')

sexo = str(input('Digite seu sexo: [M/F] ')).upper()
while sexo not in ('FM'):
    sexo = str(input('Sexo inválido, digite seu sexo novamente: '))
print(f'Seu sexo é {sexo}')

estadoCivil = str(input('Digite seu estado civil: S, C, V, D: ')).upper()
while (estadoCivil != 'S')and(estadoCivil != 'C')and(estadoCivil != 'V')and(estadoCivil != 'D'):
    print('Não tem estado civil, confuso...')
    estadoCivil = str(input('Deve ser S, C, V, D:   ')).upper()
    if estadoCivil == 'S':
        estadoCivil = 'Solteiro'
    elif estadoCivil == 'C':
        estadoCivil = 'Casado'
    elif estadoCivil == 'V':
        estadoCivil = 'Viuvo'
    else:
        estadoCivil = 'Divorciado'

print(f'Seu estado civil é {estadoCivil} ')