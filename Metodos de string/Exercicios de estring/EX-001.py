Texto1 = "Diego HOnorio Magalhaes"
Texto2 = "Diego magno mafioso"

if Texto1.upper() == Texto2.upper():
    print(Texto1)
    print(Texto2)
    print('As strings são iguais!')
else:
    print(Texto1)
    print(Texto2)
    print('O conteudo das strings são diferentes')

if len(Texto1) == len(Texto2):
    print('As strings têm o mesmo tamanho.')
else:
    print('As strings têm tamanhos diferentes.')
    
print(f'A String "{Texto1}" tem {len(Texto1)} caracteres.')
print(f'A String "{Texto2}" tem {len(Texto2)} caracteres.')
