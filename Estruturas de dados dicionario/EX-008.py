"""Exercício 3
Dada a lista de preços de produtos, uma loja resolveu fazer um reajuste nos preços dos produtos. calcule o novo valor dos produtos com base nas seguintes regras:

Preços até 1.000 vão ter um reajuste de 10% (ou seja, o novo preço será 110% do preço atual)
Preços até maiores que 1.000 até 2.000 vão ter reajuste de 15%
Preços acima de 2.000 vão ter reajuste de 20%"""


precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}

for produto, preco in precos.items():
    if preco <= 1000:
        aumento = preco * 0.10
        precos[produto] = precos[produto] + aumento
        print(f'O produto agora custa R${precos[produto]:.2f}')
    elif 1000 < preco <= 2000:
        aumento = preco * 0.15
        precos[produto] = precos[produto] + aumento
        print(f'O produto agora custa R${precos[produto]:.2f}')
    elif preco > 2000:
        aumento = preco * 0.20
        precos[produto] = precos[produto] + aumento
        print(f'O produto agora custa R${precos[produto]:.2f}')
    else:
        print('Produtos fora da faixa de aumento')
