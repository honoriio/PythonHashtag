'''9. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.'''


import os 


candidatos = ['Casimiro', 'Chico moedas', 'Super Xandão' ]
votos = [0, 0, 0, 0]

while True: 
    print('=' * 60) 
    print('URNA ELETRONICA'.center(60))
    print('=' * 60)

    print('CANDIDATOS'.center(60))
    print('-' * 60)
    
    
    print(f'[1] - {candidatos[0]} ')
    print(f'[2] - {candidatos[1]}')
    print(f'[3] - {candidatos[2]}')
    print('[4] - Para sair do programa.')
    print('-' * 60)
    resposta = int(input('Escolha: '))
    os.system('cls' if os.name == 'nt' else 'clear')

    if resposta == 1:
        votos[0] += 1
    elif resposta == 2:
       votos[1] += 1
    elif resposta == 3:
       votos[2] += 1
    elif resposta == 4:
        break
    else:
        print('Faça uma escolha valida.')

for i, candidato in enumerate(candidatos):
    print(f'Candidato: {candidatos[i]}, Votos: {votos[i]}')
