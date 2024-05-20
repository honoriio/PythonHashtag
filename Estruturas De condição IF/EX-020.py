print('=' * 60)
print('DIAS DA SEMANA'.center(60))
print('=' * 60)

Numero = int(input('Digite um número entre 1 e 7: '))
print('-' * 60)

if Numero == 1:
    print('DOMINGO'.center(60))
elif Numero == 2:
    print('SEGUNDA - FEIRA'.center(60))
elif Numero == 3:
    print('TERÇA - FEIRA'.center(60))
elif Numero == 4:
    print('QUARTA - FEIRA'.center(60))
elif Numero == 5:
    print('QUINTA - FEIRA'.center(60))
elif Numero == 6:
    print('SEXTA - FEIRA'.center(60))
elif Numero == 7:
    print('SABADO'.center(60))
else:
    print('VALOR INVALIDO!'.center(60))
print('-' * 60)