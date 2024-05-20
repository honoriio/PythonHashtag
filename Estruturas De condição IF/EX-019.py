# Cabeçalho do sistema 
print('=' * 60)
print('FOLHA DE PAGAMENTOS'.center(60))
print('=' * 60)

# Inputs do usuário
Hora = float(input('Informe quantas horas trabalhou no mês: '))
print('-' * 60)
ValorHora = float(input('Informe o valor da sua Hora R$: '))
print('-' * 60)

# Cálculo salário bruto
Bruto = (Hora * ValorHora)

# Cálculos dos descontos e FGTS

if Bruto <= 900:
    Desconto = 0
    Fgts = Bruto * 0.11 
elif Bruto <= 1500:
    Desconto = Bruto * 0.05
    Fgts = Bruto * 0.11
elif Bruto <= 2500:
    Desconto = Bruto * 0.10
    Fgts = Bruto * 0.11
else:  # Bruto > 2500
    Desconto = Bruto * 0.20
    Fgts = Bruto * 0.11

# Cálculo salário Líquido
Liquido = Bruto - Desconto

print('=' * 60)
print('DETALHAMENTOS'.center(60))
print('=' * 60)
print(f'Salário Bruto: R$ {Bruto:.2f}')
print('-' * 60)
print(f'Desconto: R$ {Desconto:.2f}')
print('-' * 60)
print(f'FGTS: R$ {Fgts:.2f} (Será depositado pela empresa.)')
print('-' * 60)
print(f'Salário Líquido: R$ {Liquido:.2f}')
print('-' * 60)