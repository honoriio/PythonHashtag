# Calculo de bonus 
# Crie um programa que calcule e de um print no bonus que os funcuionarios irão receber segundo a regra:
#A meta é 1000 vendas.
# Se o valor de vendas for maior ou igual a meta, o valor de bonus do funcuinario é 10% do valor das vendas.
# Caso contrario o valor do bonus do funcionario sera de 0.
# Print o bonus dos 3 funcionarios

# Variaveis com os valores das vendas dos funcionarios 

VendasFuncionario1 = 1000
VendasFuncionario2 = 770
VendasFuncionario3 = 2700
MetaVendas = 1000
bonus = 0

if VendasFuncionario1 >= MetaVendas:
    bonus = 0.10 * VendasFuncionario1
    print(f'O funcionario 1 Ganhou {bonus} de bonus')
else:
    bonus = 0
    print(f'O funcionario 1 Ganhou {bonus} de bonus')

if VendasFuncionario2 >= MetaVendas:
    bonus = 0.10 * VendasFuncionario2
    print(f'O funcionario 2 ganhou {bonus} de bonus')
else:
    bonus = 0
    print(f'O funcionario 2 Ganhou {bonus} de bonus')
    if VendasFuncionario3 >= MetaVendas:
        bonus = 0.10 * VendasFuncionario3
        print(f'O funcionario 3 genhou {bonus} de bonus')
    else:
        bonus = 0
        print(f'O funcionario 3 Ganhou {bonus} de bonus')

