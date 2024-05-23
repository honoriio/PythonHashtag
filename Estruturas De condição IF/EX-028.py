# Cabeçalho
print('=' * 60)
print('HIPERMERCADO TABAJARA'.center(60))
print('=' * 60)

print('PRODUTOS'.center(60))
print('=' * 60)
print('''[1] - FILE DUPLO
[2] - ALCATRA
[3] - PICANHA
''')
print('-' * 60)

Opc = int(input('Opção: '))
print('-' * 60)

if Opc == 1:
    Produto = 'FILE DUPLO'
elif Opc == 2:
    Produto = 'ALCATRA'
elif Opc == 3:
    Produto = 'PICANHA'
else:
    print('Opção invalida.')

Kg = float(input('Informe a quantia: '))
print('-' * 60)

if Produto == 'FILE DUPLO' and Kg > 5:
    Valor = Kg * 4.90
elif Produto == 'FILE DUPLO' and Kg <= 5:
    Valor = Kg * 5.80
elif Produto == 'ALCATRA' and Kg > 5:
    Valor = Kg * 5.90
elif Produto == 'ALCATRA' and Kg <= 5:
    Valor = Kg * 6.80
elif Produto == 'PICANHA' and Kg > 5:
    Valor = Kg * 6.90
elif Produto == 'PICANHA' and Kg <= 5:
    Valor = Kg * 7.80

print('=' * 60 )
print('FORMA DE PAGAMENTO'.center(60))
print('=' * 60)
print('''[1] - DINHEIRO
[2] - CARTÃO TABAJARA
''')
print('-' * 60)
Opc = int(input('Opção: '))

if Opc == 1:
    Pagamento = 'DINHEIRO'
    Total = Valor
if Opc == 2:
    Pagamento = 'CARTÃO TABAJARA'
    Desconto = (Valor * 5) / 100
    Total = Valor - Desconto


print('*' * 60)
print('CUPOM FISCAL'.center(60))
print('*' * 60)
print(f'Produto: {Produto}')
print(f'Peso.....Kg {Kg}')
print(f'Preço....R${Valor}')
print(f'Forma de Pagamento: {Pagamento}')
print(F'Valor Total R${Total}')
print('=' * 60)