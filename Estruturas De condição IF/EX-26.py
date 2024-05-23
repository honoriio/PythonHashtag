# Cabeçalho do sistema 
print('=' * 60)
print('SISTEMA DE DESCONTO DE COMBUSTIVEL'.center(60))
print('=' * 60)

# Preço de combustiveis
LitroAlcool = 1.90
LitroGasolina = 2.50


Litros = float(input('Informe a quantia de litros: '))
print('-' * 60)
print('[1] - ALCOOL')
print('[2] - GASOLINA')
print('-' * 60)
Escolha = int(input('Escolha: '))
print('-' * 60)

if Escolha == 1:
    Combustivel = 'ALCOOL'
    if Litros <= 20:
        ValorLitros = (Litros * LitroAlcool)
        Desconto = ValorLitros * 0.03
        Total = ValorLitros - Desconto

    elif Litros > 20:
        ValorLitros = (Litros * LitroAlcool)
        Desconto = ValorLitros * 0.05
        Total = ValorLitros - Desconto
    else:
        pass

elif Escolha == 2:
    Combustivel = 'GASOLINA'
    if Litros <= 20:
        ValorLitros = (Litros * LitroGasolina)
        Desconto = ValorLitros * 0.04
        Total = ValorLitros - Desconto
    elif Litros > 20:
        ValorLitros = (Litros * LitroGasolina)
        Desconto = ValorLitros * 0.06
        Total = ValorLitros - Desconto
    else:
        pass
else:
    print('Informe um valor valido.')

print(f'Quantia {Litros} litros De {Combustivel}')
print(f'Preço Bruto....................R${ValorLitros}')
print(f'Descontos......................R${Desconto}')
print(f'Preço Total....................R${Total}')
print('-' * 60)
print('=' * 60)