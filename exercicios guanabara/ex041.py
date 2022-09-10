#ate 9 anos = mirim
# ate 14 anos = infantil
#ate 19 anos = junior
#ate 25 anos = senior
#acima = master
from datetime import date

anoHoje = date.today().year
anoNascimento = int(input('Digite em que ano você nasceu: '))

mirim = 9
infantil = 14
junior = 19
senior = 25

anoAtelata = anoHoje - anoNascimento

if anoAtelata <= mirim:
    print('Classificação: Mirim ')
elif anoAtelata > mirim and anoAtelata <= infantil:
    print('Classificação: Infantil ')
elif anoAtelata > infantil and anoAtelata <= junior:
    print('Classificação: Junior ')
elif anoAtelata > junior and anoAtelata <=senior:
    print('Classificação: Seniôr ')
else:
    print('Classificação: Master')