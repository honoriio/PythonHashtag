# Cabeçalho do sistema 

print('=' * 60)
print('INVESTIGAÇÃO'.center(60))
print('=' * 60)

# Campo da perguntas
print('PERGUNTAS'.center(60))
print('-' * 60)

# Primeira pergunta
print('Telefonou para a vitima?')
Resposta1 = input('Resposta: ').upper()
print('-' * 60)

# Segunda pergunta
print('Entrou no local do crime?')
Resposta2 = input('Resposta: ').upper()
print('-' * 60)

# Terceira pergunta
print('Mora perto da vitima?')
Resposta3 = input('Resposta: ').upper()
print('-' * 60)

# Quarta pergunta
print('Devia dinheiro para a vitma?')
Resposta4 = input('Resposta: ').upper()
print('-' * 60)

# Quinta pergunta
print('Trabalhou com a vitima?')
Resposta5 = input('Resposta: ').upper()
print('-' * 60)

if Resposta1 == 'SIM':
    Resposta1 = 1
else: 
    Resposta1 = 0
if Resposta2 == 'SIM':
    Resposta2 = 1
else:
    Resposta2 = 0
if Resposta3 == 'SIM':
    Resposta3 = 1
else:
    Resposta3 = 0
if Resposta4 == 'SIM':
    Resposta4 = 1
else: Resposta4 = 0
if Resposta5 == 'SIM':
    Resposta5 = 1
else:
    Resposta5 = 0

Total = (Resposta1 + Resposta2 + Resposta3 + Resposta4 + Resposta5)

if Total == 2:
    print('SUSPEITO')
elif Total >=3 and Total <= 4:
    print('CÚMPLICE')
elif Total == 5:
    print('ASSASINO')
else:
    print('INOCENTE')
print('-' * 60)