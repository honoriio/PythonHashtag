'''12. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário desse funcionário em 2003. '''


anos_de_aumento = 2003 - 1997

salario_inicial = 1000.15
porcentagem = 0.015

for i in range(anos_de_aumento):
    i += 1
    porcentagem += porcentagem
    acrescimo = (salario_inicial * porcentagem) / 100
    salario_final = (salario_inicial + acrescimo)

print(f'O salario do funcionario em 1997 foi de R${salario_inicial:,.2f}')
print(f'O salario do funcionaio em 2003 foi de R${salario_final:,.2f}')