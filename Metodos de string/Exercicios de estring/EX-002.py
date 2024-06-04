numero = input('Informe um numero de telefone: ')
digitoExtra = "3"


if len(numero) == 7:
    numero += digitoExtra
    numeroFormatado = numero[:4] + "-" + numero[4:]
    print(f'Telefone corrigico sem formatação: {numero}')
    print(f'Telefone corrigido com formatação: {numeroFormatado}')
else:
    print('O telefone não tem 7 digitos.')

