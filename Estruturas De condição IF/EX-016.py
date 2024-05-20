numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
numero3 = int(input('INforme o terceiro número: '))

# Descobrindo o mario numero
if numero1 == numero2 and numero1 == numero3:
    print(numero1)
    print(numero2)
    print(numero3)
elif numero1 >= numero2 and numero1 == numero3:
    maiorNumero = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    maiorNumero = numero2
else:
    maiorNumero = numero3

# Descobrindo o menor numero

if numero1 <= numero2 and numero1 <= numero3:
    menorNumero = numero1
elif numero2 <= numero1 and numero2 <= numero3:
    menorNumero = numero2
else: 
    menorNumero = numero3

# Descobrindo o numero medio
if numero1 < maiorNumero and numero1 > menorNumero:
    medioNumero = numero1
elif numero2 < maiorNumero and numero2 > menorNumero:
    medioNumero = numero2
else:
    medioNumero = numero3

print('Números em ordem decrescente: ')
print(maiorNumero)
print(medioNumero)
print(menorNumero)