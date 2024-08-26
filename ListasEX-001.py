produtos = ["carro", "moto", "bike", "patinete"]
quantia = [30, 50, 25, 15]

produto = input('Informe o Produto: ')

if produto in produtos:
    i = produtos.index(produto)
    item = produtos[i]
    unidades = quantia[i]
    print(f'Produto: {item}, Quantia: {unidades}')
else:
    print('O produto informado não existe em nossa base de dados.')
