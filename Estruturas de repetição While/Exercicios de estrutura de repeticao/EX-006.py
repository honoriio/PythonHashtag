'''6. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o maior faturamento'''

faturamentos = []

for i in range(5):
    mes = i + 1
    faturamento = float(input(f'Informe o Faturamento do {mes}° mês: '))
    faturamentos.append([faturamento])

maior = max(faturamentos)
indice = faturamentos.index(maior) + 1

print(f'O maior faturamento foi do {indice}° Mês, com o valor de R${maior[0]:,.2f} ')
    