meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

metas_batidas = []
for venda in vendas:
   if venda[1] >= meta:
      metas_batidas.append(venda)

porcentagem = (len(metas_batidas) / len(vendas))

print(f'{porcentagem:.1%}')