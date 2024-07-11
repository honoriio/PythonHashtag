'''Exercício 1
Crie um sistema de consulta de preços Seu sistema deve:

Pedir para o usuário o nome de um produto
Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta - Ex: O produto celular custa R$1500
Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente'''


precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

nome = input('Informe o nome do produto: ')

if nome in precos:
    print(f'O Produto {precos[nome]} custa R${precos[nome]:.2f}')
else:
    print('O produto pesquisado não existe em nossa base da dados...')
