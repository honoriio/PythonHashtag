# Cabeçalho do sistema
print('=' * 60)
print('ORGANIZAÇÕES TABAJARA'.center(60))
print('=' * 60)

# Valores elegiveis para aumento
criterio1 = 280
criterio2 = 700
criterio3 = 1500

salario = float(input('Informe o salario R$: '))

if salario:
    if salario <= criterio1:
        aumento = salario * 0.20
        salarioNovo = salario + aumento
    elif salario >= criterio1 and salario <= criterio2:
        aumento = salario * 0.15
        salarioNovo = salario + aumento
    elif salario > criterio2 and salario <= criterio3:
        aumento = salario * 0.10
        salarioNovo = salario + aumento
    elif salario > criterio3:
        aumento = salario * 0.05
        salarioNovo = salario + aumento
    else:
        print('Preencha os campos corretamente')

print(f'O seu salario atual e de R${salario}')
print(f'O seu novo salario e de R${salarioNovo}')