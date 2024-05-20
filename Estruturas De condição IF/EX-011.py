media = 7
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

mediaAluno = (nota1 + nota2) / 2

if mediaAluno:
    if mediaAluno == 10:
        print(f'MEDIA {mediaAluno} APROVADO COM DISTINÇÃO')
    elif mediaAluno >= media:
        print(f'MEDIA {mediaAluno} APROVADO')
    elif mediaAluno < media:
        print(f'MEDIA {mediaAluno} REPROVADO')

    else:
        print('Por favor, informe as notas ')
else:
    print('Por favor, preencha os campos corretamente')