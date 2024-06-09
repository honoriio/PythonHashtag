'''Exercício 2
Crie um sistema de consulta de preços

Seu sistema deve:

    Pedir para o usuário o nome de um produto
    Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta - Ex: O produto celular custa R$1500
    Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente

'''

produtos = ["celular", "camera", "fone de ouvido", "monitor"]
precos = [1500, 1000, 800, 2000]


NomeProduto = input('Informe o nome do produto: ').lower()

if NomeProduto in produtos:
    indice = produtos.index(NomeProduto)
    Produto = produtos[indice]
    Preco = precos[indice]

    print(f'O produto: {Produto} Custa: R${Preco:,.2f}')

else:
    print('Produto não encontrado na lista de produtos, temte novamente.')
