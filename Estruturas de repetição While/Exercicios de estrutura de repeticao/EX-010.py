'''10. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
 O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''


cds = int(input('Informe a quantia de cds: '))
preco = []

for i in range(cds):
    valor = float(input('Informe o preço pago para cada cd: '))
    preco.append(valor)

total_gasto = sum(preco)

media = (total_gasto / cds)

print(f'A coleção contem {cds} Exemplares de Cds')
print(f'O valor total da coleção e de: R${total_gasto:,.2f}')
print(f'O Valor medio de cada CD e de: R${media:,.2f}')