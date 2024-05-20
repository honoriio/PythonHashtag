estadoCivil = input('Informe seu estado civil: ').upper()

if estadoCivil:
    if estadoCivil == 'C':
        print('CASADO')
    elif estadoCivil == 'S':
        print('SOLTEIRO')
    elif estadoCivil == 'D':
        print('DIVORCIADO')
    elif estadoCivil == 'V':
        print('VIUVO')
    elif estadoCivil == 'O':
        print('OUTROS')
    else:
        print('Informe um valor valido.')
else:
    print('Preencha os campos corretamente')