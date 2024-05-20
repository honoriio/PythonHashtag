#Cabeçalho sistema

print('=' * 60)
print('MEDIA DE NOTAS'.center(60))
print('=' * 60)

# Inputs das notas dos alunos 

Nota1 = float(input('Informe a primeira nota: '))
print('-' * 60)
Nota2 = float(input('Informe a segunda nota: '))
print('-' * 60)
Nota3 = float(input('Informe a terceira nota: '))
print('=' * 60)

# Media das notas

Media = (Nota1 + Nota2 + Nota3) / 3

if Media == 10:
    Situacao = 'APROVADO COM DISTINÇÃO'
elif Media >= 7:
    Situacao = 'APROVADO'
elif Media < 7:
    Situacao = 'REPROVADO'
else:
    print('VALOR INSERIDO INVALIDO.')
    print('-' * 60)

print(f'Sua media e de {Media:.2f} Pontos.')
print('-' * 60)
print(f'Voce foi: {Situacao}')
print('=' * 60)