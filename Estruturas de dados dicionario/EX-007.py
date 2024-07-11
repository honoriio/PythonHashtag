""" Exercício 2
Agora edite o programa anterior para fazer com que, caso não exista o produto, o programa pergunte se o usuário quer cadastrar o produto
Se ele responder sim, o programa deve pedir o nome do produto e o preco do produto e cadastrar no dicionário de preços
Em seguida do cadastro bem sucedido, o programa deve printar o dicionário de precos atualizado """

precos = {}

resposta = input('Deseja cadastrar um produto?: ').upper()

if resposta == 'SIM' or resposta == 'S':
    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o valor: R$ '))

    precos[nome] = preco

    print('-' * 120)
    print('Cadastro bem sucedido...')
    print('-' * 120)
    for produto, valor in precos.items():
        print(f'O produto {produto} tem o valor: R${valor:,.2f}')
else:
    print('Porgrama finalizado...')
