'''7. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o faturamento total (soma) e o faturamento médio por mês (média).'''


faturamentos = []

for i in range(5):
    mes = i + 1
    faturamento = float(input(f'Informe o  faturamento do {mes}° mês R$: '))
    faturamentos.append(faturamento)

#Aqui foi utilizado uma compressão de lista para desconpactar os itens e fazer a soma (vou pesquisar depois)
faturamento_total = sum(faturamentos) 

faturamento_medio = (faturamento_total / len(faturamentos))

print(f'O faturamento total foi de: R${faturamento_total:,.2f}')
print(f'O faturamento medio foi de: R${faturamento_medio:,.2f}')
