produto1 = float(input('Qual o preço do primeiro produto?:  '))
produto2 = float(input('Qual o preço do Segundo produto?:  '))
produto3 = float(input('Qual o preço do Terceiro produto?:  '))

if produto1 <= produto2 and produto1 <= produto3:
    print('Compre o produto 1, pois ele e o mais barato')
    print(f'Preço produto 1 R${produto1}')
elif produto2 <= produto1 and produto2 <= produto3:
    print('Compre o produto 2, pois ele e o mais barato')
    print(f'Preço produto 2 R${produto2}')
else:
    print('Compre o produto 3, pois ele e o mais barato')
    print(f'Preço produto 3 R${produto3}')

