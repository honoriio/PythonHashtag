# Cabeçalho programa

print('=' * 60)
print('CONTROLE DE PESO DE PEIXES'.center(60))
print('=' * 60)

#Inputs do usuario
Peso = float(input('Informe o peso: '))
print('=' * 60)

#Limite de peso 
PesoLimite = 50

# Multa por excesso de peso
Multa = 4

# Calculo do peso 

if Peso > PesoLimite:
    PesoExcedente = (Peso - PesoLimite)
    MultaExcesso = (PesoExcedente * Multa)
    print(f'O peso Informado de {Peso} Kg ')
    print('-' * 60)
    print(f'Peso excedido {PesoExcedente} kg')
    print('-' * 60)
    print(f'Multa por Kg excedido: {MultaExcesso}')
    print('=' * 60)
else:
    print('O peso não ultrapassa o Peso limite.')
    print('=' * 60)
