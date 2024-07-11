"""Exercício 5
Uma empresa está analisando os resultados de vendas do 1º semestre de 2022 e 2023
Qual foi o % de crescimento de cada mês de 2023 em relação a 2022?
Depois de calcular isso, calcule o valor total de crescimento de 2023 em relação a 2022"""


vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

for mes in vendas_23:
    valor22 = vendas_22[mes]
    valor23 = vendas_23[mes]

    percentual = (valor23/valor22) - 1

    print(f'Em {mes}, A variaçao de percentual foi de: {percentual:.1%}')


total22 = sum(vendas_22.values())
total23 = sum(vendas_23.values())
crescimento = total23/total22 - 1

print(f'O cresimento real foi de {crescimento:.2%}')
