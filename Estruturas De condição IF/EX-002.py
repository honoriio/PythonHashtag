
meta = 0.05
taxa = 0
redimento = 0.25

if redimento >meta:
    if redimento > 0.20:
        taxa = 0.04
        print('Seu retorno foi mario que 20 Porcento, A taxa cobrada sera de 4 porcento.')
    else:
        taxa = 0.02
        print(f'Sera cobrado uma taxa de {taxa} % sobre o valor de retorno ')
else:
    print('Seu retorno foi menor que 0.05 Porcento e não sera cobrado taxa.')