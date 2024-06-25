'''5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.'''

populacaoA = float(input('Informe a quantia de Hábitantes da população A: '))
taxaA = float(input('Informe a taxa de crescimento para a população A: '))
populacaoB = float(input('Informe a quantia de Hábitantes da população B: '))
taxaB = float(input('Informe a taxa de crescimento para a população B: '))



contador = 0

while populacaoA <= populacaoB:
    contador += 1
    crescimentoA = populacaoA * taxaA
    populacaoA = populacaoA + crescimentoA
    
    crescimentoB = populacaoB * taxaB
    populacaoB = populacaoB + crescimentoB




print(f'A população A levou {contador} Anos para atingir a quantia da população B.')
print(f'População A {populacaoA:,.0f} Hábitantes')
print(f'População B {populacaoB:,.0f} Hábitantes')



"""Lembrando que, não tem verificação, então o programa pode ser executado em um loop infinito caso a população A nunca alcance a população B"""