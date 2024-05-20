valor = int(input('Informe o valor a ser sacado: '))

n100 = 0
n50 = 0
n10 = 0
n5 = 0
n1 = 0

if 10 <= valor <= 600:
    print('São necessárias:')
    if valor >= 100:
        n100 = valor // 100
        print(n100, 'notas de 100')
    if valor % 100 >= 50:
        n50 = (valor - 100*n100) // 50
        print(n50, 'notas de 50')
    if valor % 50 >= 10:
        n10 = (valor - 100*n100 - 50*n50) // 10
        print(n10, 'notas de 10')
    if valor % 10 >= 5:
        n5 = (valor - 100*n100 - 50*n50 - 10*n10) // 5
        print(n5, 'notas de 5')
    if valor % 5 >= 1:
        n1 = valor - 100*n100 - 50*n50 - 10*n10 - 5*n5
        print(n1, 'notas de 1')
else:
    print('Informe um valor entre 10 e 600 reais')