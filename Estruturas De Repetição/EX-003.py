bebidas = [
    "Coca-Cola",
    "Pepsi",
    "Guaraná Antarctica",
    "Sprite",
    "Fanta",
    "Red Bull",
    "Monster Energy",
    "Burn",
    "Schweppes",
    "Dolly"
]

quantidade_estoque = [50, 40, 60, 30, 25, 70, 35, 55, 20, 15]


for i, bebida in enumerate(bebidas):
    if quantidade_estoque[i] < 50:
         print(f'{bebidas[i]} está abaixo do nível mínimo de 50 unidades. Temos em estoque {quantidade_estoque[i]} unidades.')