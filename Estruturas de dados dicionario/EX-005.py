produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

tuplas_vendas = zip(vendas2019, vendas2020)

tuplas_produtos = zip(produtos, tuplas_vendas)

dicionario_produtos = dict(tuplas_produtos)

for produtos, valores in dicionario_produtos.items():
    print(f'Produto: {produtos}, Vendas 2019 R${valores[0]:,.2f}, Vendas 2020 R${valores[1]:,.2f}')
