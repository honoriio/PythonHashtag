'''1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''

while True:
    print('Informe uma nota entre 0 e 10: ')
    nota = int(input('Nota: '))
    if nota >= 0 and nota <= 10:
        print('Valor informado correto')
        break
    else:
        print('O valor informado está fora do intervalo de 0 a 10, por favor insira um valor valido.')