'''8. Faça um programa que consiga categorizar a idade das equipes de uma empresa.
 Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da equipe varia,
 entre 0 e 25 (jovem) ,26 e 60 (sênior) e maior que 60 (idosa); e então, dizer se a equipe é jovem, sênior ou idosa, conforme a média calculada'''

contador = 0
idades = []
while True:
    contador += 1
    idade = int(input('Informe a sua idade: '))
    idades.append(idade)
    resposta = input('Deseja continuar?: ').upper()

    if resposta == "NAO" or resposta == "N":
        break


media = (sum(idades) / contador)

if 0 <=  media <= 26:
    print(f'A media de idade da equipe e {media} anos e se enquandra no publico JOVEM.')

elif 26 < media <= 60:
    print(f'A media de idade da equipe e {media} anos e se enquadra no publico SÊNIOR.')

elif media > 60:
    print(f'A media de idade da equipe e {media} anos e se enquadra no publico IDOSO.')

else:
    print('Não foi possivel calcular a media da equipe.')
