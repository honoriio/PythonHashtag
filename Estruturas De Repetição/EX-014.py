'''4.Em quais meses a média de temperatura foi maior do que a média nacional?'''

meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
]

temperaturas = [30, 29, 28, 28, 25, 26, 20, 21, 19, 25, 27, 32]

media_temperatura = (sum(temperaturas) / len(temperaturas))

for i, mes in enumerate(meses):
    if temperaturas[i] > media_temperatura:
        print('-' * 60)
        print(f'Mês acima da media nacional: {meses[i]}, Temperatura {temperaturas[i]}°')

print('=' * 60)
print(f'A media nacional foi de {media_temperatura:.2f}º'.center(60))
print('=' * 60)