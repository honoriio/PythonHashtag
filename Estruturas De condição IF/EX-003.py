# Treinando elif

meta = 20000
vendas = 25000
bonus = 0

if vendas < meta:
    print('Não Tem Bonus')
elif vendas > (meta * 2):
    bonus = 0.07 * vendas
    print(f'Seu Bonus e de {bonus}')
else:
    bonus = 0.03 * vendas
    print(f'Seu bonus e de {bonus}')