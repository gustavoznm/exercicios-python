from datetime import date


anoHoje = date.today().year
ano_nascimento = int(input('Digite o Ano em que você nasceu: '))
idade = (anoHoje - ano_nascimento)

print(f'Quem nasceu em {ano_nascimento} tem {idade} em {anoHoje}! ')

if idade == 18:
    print('Você tem que se alistar imediantamente! ')
elif idade < 18:
    idadesaldo = 18 - idade
    anoalistamento = ano_nascimento + 18
    print(f' Ainda faltam {idadesaldo} anos para você se alistar. ')
    print(f' Seu alistamento é em {anoalistamento} ')

elif idade > 18:
    idadesaldo = idade - 18
    anoalistamento = ano_nascimento + 18
    print(f' Você ja deveria ter se alistado há {idadesaldo} anos')
    print(f' Seu alistamento foi em {anoalistamento}')


