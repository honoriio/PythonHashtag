produto = ["tv", "celular", "tablet", "mouse", "teclado", "geladeira", "forno"]

estoque = [100, 150, 100, 120, 70, 90, 80]

i = produto.index('geladeira')

item = produto[i]
quantia = estoque[i]

print(f'Produto: {item}, Estoque: {quantia}')