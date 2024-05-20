orcamento1 = float(input('Informe o primeiro orçamento: '))
orcamento2 = float(input('Informe o Segundo orçamento: '))
orcamento3 = float(input('Informe o Terceiro orçamento: '))

if orcamento1 == orcamento2 and orcamento1 == orcamento3:
    print('O três orçamentos são iguais.')
elif orcamento1 > orcamento2 and orcamento1 > orcamento3:
    print('O orçamento 1 e maior')
elif orcamento2 > orcamento1 and orcamento2 > orcamento3:
    print('O orçamento 2 e maior')
elif orcamento3 > orcamento1 and orcamento3 > orcamento2:
    print('O orçamento 3 e o maior')
else:
    print('A orcamentos iguais, porem não os três')