'''13. O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
 Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.'''

import os

total = 0
while True:
    print('=' * 60)
    print('CARDAPIO'.center(60))
    print('=' * 60)

    print('-' * 60)
    print('''    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00''')
    print('-' * 60)
    print('[1] - Para finalizar o pedido.')
    print('-' * 60)

    codigo = int(input('Informe o codigo do item: '))

    if codigo == 100:
        quantidade = int(input('Informe a quantia: '))
        total += 1.20 * quantidade
    elif codigo == 101:
        quantidade = int(input('Informe a quantia: '))
        total += 1.30 * quantidade
    elif codigo == 102:
        quantidade = int(input('Informe a quantia: '))
        total += 1.50 * quantidade
    elif codigo == 103:
        quantidade = int(input('Informe a quantia: '))
        total += 1.20 * quantidade
    elif codigo == 104:
        quantidade = int(input('Informe a quantia: '))
        total += 1.30 * quantidade
    elif codigo == 105:
        quantidade = int(input('Informe a quantia: '))
        total += 1.00 * quantidade
    elif codigo == 1:
        break
    os.system('cls' if os.name == 'nt' else 'clear')

print('=' * 60)
print(f'O total foi de R${total:,.2f}'.center(60))
print('=' * 60)