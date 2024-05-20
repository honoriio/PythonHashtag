# Cabeçalho do sistema
print('=' * 60)
print('MEDIA DE NOTAS'.center(60))
print('=' * 60)

# Inputs do usuário
Nota1 = float(input('Informe a primeira nota: '))
Nota2 = float(input('Informe a segunda nota: '))
print('-' * 60)

# Cálculo da média
Media = (Nota1 + Nota2) / 2

# Condições para média de aproveitamento
if 9 <= Media <= 10:
    aproveitamento = 'A'
elif 7.5 <= Media < 9:
    aproveitamento = 'B'
elif 6 <= Media < 7.5:
    aproveitamento = 'C'
elif 4 <= Media < 6:
    aproveitamento = 'D'
else:
    aproveitamento = 'E'

# Exibição do resultado
print(f'Sua média foi de {Media:.2f} pontos')
print('-' * 60)
print(f'Seu aproveitamento foi Classe: {aproveitamento}')
print('-' * 60)
