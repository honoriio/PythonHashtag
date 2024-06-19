'''1. Faça um Programa que leia as vendas dos vendedores, mostre a venda de cada vendedor com o seu nome e a média de vendas'''

vendas = [1000, 1500, 1200, 1300]
vendedores = ["Fulano", "Beltrano", "Ciclano", "Lira"]


for i, venda in enumerate(vendas):
    print(f'Vendedor: {vendedores[i]} Valor em vendas: R${venda:.2f}')

media = sum(vendas) / len(vendas)

print('=' * 120)
print(f'A media de vendas e R${media:.2f}'.center(120))
print('=' * 120)
