'''2. Faça um Programa que crie uma lista com as médias de cada aluno, imprima as médias de cada aluno e a quantidade de alunos com média maior que 7.'''

alunos = ["José", "Joana", "Maria", "Carla", "Mauricio", "Andre", "Tiago", "Enzo", "Amanda", "Alessandra"]
notas = [
    [10, 9, 8, 8],
    [9, 7, 6, 4],
    [10, 10, 10, 10],
    [5, 3, 10, 9],
    [7, 6, 6, 6],
    [7, 7, 8, 7],
    [7, 7, 7, 9],
    [8, 5, 6, 7],
    [10, 9, 7, 4],
    [10, 1, 3, 3],
]

medias = []
maior_7 = 0

print('=' * 60)
print('MEDIA'.center(60))
print('=' * 60)
for i in range(len(alunos)):
    soma_notas = sum(notas[i])
    media = (soma_notas / len(notas[i]))
    medias.append(media)
    if media >= 7:
        maior_7 += 1

for i, aluno in enumerate(alunos):
    print('-' * 60)
    print(f'Nome: {aluno}, Media: {medias[i]}')

print('=' * 60) 
print(f'O total de {maior_7} Alunos Tem a media acima de 7.')
print('=' * 60)

