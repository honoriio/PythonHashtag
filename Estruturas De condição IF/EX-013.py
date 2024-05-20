orcamento1 = float(input('Informe o primeiro orçamento: '))
orcamento2 = float(input('Informe o Segundo orçamento: '))
orcamento3 = float(input('Informe o Terceiro orçamento: '))

if orcamento1 == orcamento2 and orcamento1 == orcamento3:
    print('O três orçamentos são iguais.')
elif orcamento1 >= orcamento2 and orcamento1 >= orcamento3:
    maior = orcamento1
elif orcamento2 >= orcamento1 and orcamento2 >= orcamento3:
    maior = orcamento2
else:
    maior = orcamento3


if orcamento1 <= orcamento2 and orcamento1 <= orcamento3:
    menor = orcamento1
elif orcamento2 <= orcamento1 and orcamento2 <= orcamento3:
    menor = orcamento2
else: 
    menor = orcamento3


print(f'Maior Orçamento {maior}')
print(f'Menor orçamento {menor}')