nota_funcionario = 9
meta_nota = 9

meta_loja = 10000
meta_funcinario = 3000
vendas_funcionario = 5000
vendas_loja = 5000
bonus = 0

if nota_funcionario >= meta_nota or (vendas_loja > meta_loja and vendas_funcionario > meta_funcinario):
    bonus = 0.03 * vendas_funcionario
    print(f'Seu Bonus e de {bonus}')
else:
    print('Não tem bonus')