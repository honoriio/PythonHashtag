'''7. Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
 Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:'''

vendas = [1000, 2000, 3000, 4000, 5000, 6000, 5500, 4500, 3600]
pagamento_semana = 200
porcento = 0.09
for i, venda in enumerate(vendas):
    pagamento_total = (pagamento_semana + porcento * vendas[i])
    print(pagamento_total)

    