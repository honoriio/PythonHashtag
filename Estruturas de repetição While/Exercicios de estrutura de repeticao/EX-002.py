'''2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''

credenciais = []

while True:
    nome = input('Nome de usuario: ')
    senha = input('senha: ')
    credenciais.append([nome, senha])
    if credenciais[-1][0] == credenciais[-1][1]:
        print('A senha informada e a mesma que o nome de usuario, informe uma senha diferente do nome de usuario.')
    else:
        print('Usuario e senha cadastrados com sucesso!.')
        break
        