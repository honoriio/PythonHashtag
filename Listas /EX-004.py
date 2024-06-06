meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

top3 = []

vendas_ano = vendas_1sem + vendas_2sem

for i in range(3):
    maior = max(vendas_ano)
    top3.append(maior)
    vendas_ano.remove(maior)

print(top3)

