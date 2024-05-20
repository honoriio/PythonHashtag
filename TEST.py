senhas = [123456 , 2593, 5575, 6535]
senha = int(input('Informe a sua senha: '))

if senha in senhas:
    print('Login liberado')
else:
    print('A senha informada esta incorreta. ')