funcionarios = ['Lira', 'João', 'Diego', 'Alon']
produtos = ['ipad', 'iphone']
vendas = [
    [100, 200],
    [300, 500],
    [50, 1000],
    [900, 10],
]

print('=' * 60)
Vendedor = input('Informe o vendedor: ')
print('-' * 60)
produto = input('Informe o produto: ')
print('-' * 60)

indice_vendedor = funcionarios.index(Vendedor)
indice_produto = produtos.index(produto)

nome_vendedor = funcionarios[indice_vendedor]
nome_produto = produtos[indice_produto]

funionario = funcionarios[indice_vendedor]
vendas_funcionario = vendas[indice_vendedor]
vendas_produto = vendas_funcionario[indice_produto]

print('-' * 60)
print(f'O vendedor {nome_vendedor} Vendeu R${vendas_produto:,.2f} do produto {nome_produto}')
