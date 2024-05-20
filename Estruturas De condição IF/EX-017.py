print('=' * 60)
print('[M] - MATUTINO (MANHÃ)')
print('[V] - VESPERTINO (TARDE)')
print('[N] - NOTURNO (NOITE)')
print('=' * 60)
turno = input('Informe em que turno você estuda: ').upper()
print('-' * 60)

if turno:
    if turno == 'M':
        print('Bom Dia!')
    elif turno == 'V':
        print('Boa Tarde!')
    elif turno == 'N':
        print('Boa Noite!')
    else:
        print('Valor invalido!')

