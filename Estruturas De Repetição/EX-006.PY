# Precisei usar o gabarito, cabeça bugou na hora 

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

for venda in vendas:
    if venda[1] > meta:
        print(f'O vendedor {venda[0]} vendeu {venda[1]}')