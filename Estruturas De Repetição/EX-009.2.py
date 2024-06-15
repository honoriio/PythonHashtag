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


# Descobrindo qual foi o vendedor que mais vendeu 
maior_vendedor = ''
maior_venda = 0
for venda in vendas:
    if venda[1] > maior_venda:
        maior_venda = venda[1]
        maior_vendedor = venda[0]


print(f'{porcentagem:.1%} Dos vendedores atingitam a meta')
print(f'O maior vendedor foi {maior_vendedor} com {maior_venda} em vendas.')