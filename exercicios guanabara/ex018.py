from math import radians, sin, cos, tan

angulo = float(input('Digite um angulo qualquer! '))
sen = sin(radians(angulo))
print(f'O angulo de {angulo} tem o seno de {sen} ')
coss = cos(radians(angulo))
print(f'O angulo de {angulo} tem o cosseno de {coss}')
tan = tan(radians(angulo))
print(f'O angulo de {angulo} tem a tangente de {tan}')