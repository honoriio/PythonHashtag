# Cabeçalho do programa 
print('=' * 60)
print('FRUTERIA'.center(60))
print('=' * 60)

print('[1] - MORANGO')
print('[2] - MAÇA')
print('=' * 60)
Opc = int(input('Opção: '))

if Opc == 1:
    Fruta = 'MORANGO'
elif Opc == 2:
    Fruta = 'MAÇA'
else:
    print('Valor informado errado.')
print('-' * 60)
Kg = float(input('Kilos: '))
print('-' * 60)

if Fruta == 'MORANGO':
    Valor = Kg * 2.50
    if Kg <= 5:
        Valor = Kg * 2,50
        Total = Valor
    elif Kg > 5 and Kg <= 8:
        Valor = Kg * 2.20
        Total = Valor
    elif Kg > 8 or Valor > 25:
        Desconto = (Valor * 10) / 100
        Total = (Valor - Desconto)

print(Desconto, Total, Fruta)




#Fazer analise e melhorar o programa 
