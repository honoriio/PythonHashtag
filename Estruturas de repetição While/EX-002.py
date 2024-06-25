'''1. Input até o usuário parar
Vamos criar um sistema de vendas. Nosso programa deve registrar os produtos e as quantidades (2 inputs) e adicionar em uma lista.

O programa deve continuar rodando até o input ser vazio, ou seja, o usuário apertar enter sem digitar nenhum produto ou quantidade.

Ao final do programa, ele deve printar todos os produtos e quantidades vendidas.

Obs: Caso queira, para o print ficar mais visual, pode usar o join para cada item ser printado em uma linha. Sugestão para sua lista de produtos vendidos:'''


vendas = [
    ['maçã', 5],
    ['banana', 15],
    ['azeite', 1],
    ['vinho', 3],
]

while True:
    produto = input('Informe o produto desejado: ')
    quantidade = input('informe a quantidade desejada: ')
    if produto == "" or quantidade == "":
        break
    else: 
        vendas.append([produto, quantidade])
string_vendas = [f"{venda[0]}: {venda[1]}" for venda in vendas]
formatado = ", ".join(string_vendas)
print(f'Vendas: {formatado}')

