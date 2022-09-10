#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações
print('=' * 25)
usuario = str(input('Digite seu usuario: '))
senha = str(input('Digite uma senha: '))
while usuario == senha:
    print('=' * 13, 'ERRO', '=' * 13)
    print('Usuario e senha são iguais!!')
    print('=' * 13, 'ERRO', '=' * 13)
    usuario = str(input('Digite seu usuario: '))
    senha = str(input('Digite uma senha: '))
print(f'Usuario e senha criados, para acessar sua conta basta usar o usuario : ({usuario}) e a senha: ({senha})')
