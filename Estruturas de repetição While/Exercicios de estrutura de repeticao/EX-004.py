'''4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
 Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''

populacaoA = 80000
populacaoB = 200000

contador = 0

while populacaoA <= populacaoB:
    contador += 1
    crescimento = populacaoA * 0.03
    populacaoA = populacaoA + crescimento
    
    crescimento2 = populacaoB * 0.015
    populacaoB = populacaoB + crescimento2


print(f'A população A levou {contador} Anos para atingir a quantia da população B.')
print(f'População A {populacaoA:,.0f} Hábitantes')
print(f'População B {populacaoB:,.0f} Hábitantes')