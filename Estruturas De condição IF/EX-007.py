# Cabeçalho do programa
print('=' * 60)
print('GERENCIADOR DE MERCADORIA'.center(60))
print('=' * 60)

# Sessão de input
print('-' * 60)
NomeProduto = input('Qual o nome do produto: ')
print('-' * 60)
print('Qual a categoria do produto.')
while True:
    print('-' * 60)
    print('[1] - ALIMENTOS')
    print('[2] - BEBIDAS')
    print('[3] - LIMPEZA')
    print('-' * 60)
    opc = input('Opção: ')

    if opc == '1':
        CategoriaProdutos = 'ALIMENTOS'
        break
    elif opc == '2':
        CategoriaProdutos = 'BEBIDAS'
        break
    elif opc == '3':
        CategoriaProdutos = 'LIMPEZA'
        break
    else: 
        print('Por favor, informe uma opção valida. ')

print('-' * 60)
QuantiaEmEstoque = int(input('Informe a quantia do produto: '))
print('-' * 60)


#Quantias minimas em estoque por categoria
QuantiaMinimaAlimentos = 50
QuantiaMinimaBebidas = 75
QuantiaMinimaLimpeza = 30

# Condições de verificações do programa
if CategoriaProdutos == 'ALIMENTOS':
    if QuantiaEmEstoque < QuantiaMinimaAlimentos:
        print(f'Quantia em estoque do produto: {NomeProduto} está abaixo do estoque minimo.')
        print('Favor abrir pedido de compra')
    else:
        pass
if CategoriaProdutos == 'BEBIDAS':
    if QuantiaEmEstoque < QuantiaMinimaBebidas:
        print(f'Quantia em estoque do produto: {NomeProduto} está abaixo do estoque minimo.')
        print('Favor abrir pedido de compra')
    else:
        pass
if CategoriaProdutos == 'LIMPEZA':
    if QuantiaEmEstoque < QuantiaMinimaLimpeza:
        print(f'Quantia em estoque do produto: {NomeProduto} está abaixo do estoque minimo.')
        print('Favor abrir pedido de compra')
    else:
        pass
else:
    pass