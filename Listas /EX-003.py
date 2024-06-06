meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_ano = vendas_1sem + vendas_2sem


maior = max(vendas_ano)
menor = min(vendas_ano)

i1 = vendas_ano.index(maior)
i2 = vendas_ano.index(menor)

mes1 = meses[i1]
mes2 = meses[i2]


# Descobrindo o faturamento total de vendas do ano 

faturamento_total = sum(vendas_ano)

percentual = maior / faturamento_total

print(f'O melhor mes para vendas foi {mes1} com o total de R${maior:,.2f} vendas.')
print(f'O pior mes de para vendas foi {mes2} com o total de R${menor:,.2f} vendas.')
print(f'O faturamento total foi de R${faturamento_total:,.2f}')
print(f'O melhor mes {mes1}, contribuiu com {percentual:.1%} no faturamento anual.')
