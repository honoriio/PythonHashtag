produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

#cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

#Achando o indice do produto livro, valores e quantias vendidas 
IndiceProduto = produtos.index('livro')
IndicePreco = produtos_ecommerce[IndiceProduto]
Quantia = IndicePreco[0]
valor = IndicePreco[1]



# Calculo dos juros encima do valor dos livros.
Juros = (valor * 10) / 100

# Atribuindo o valor do juros ao produto

ValorComJuros = (valor + Juros)

#Aualizando o valor dos juros ao item 

produtos_ecommerce.pop(IndiceProduto)
NovoPreco = [Quantia, ValorComJuros]
produtos_ecommerce[IndiceProduto] = produtos_ecommerce[IndiceProduto] = NovoPreco

CustoAntigo = (Quantia * valor)
NovoCusto = (Quantia * ValorComJuros)
Aumento = (NovoCusto - CustoAntigo)

print('=' * 120)
print(f'Tabela atualizada'.center(120))
print('=' * 120)
print(produtos)
print('-' * 120)
print(produtos_ecommerce)

print('=' * 120)
print(f'Com o novo imposto o novo custo sera de R${ValorComJuros:.2f}')
print('-' * 120)
print(f'O custo antigo era de R${ValorComJuros:.2f}')
print('=' * 120)
print('Sendo assim, o custo total sera de')
print(f'R${NovoCusto:,.2f}')
print('-' * 120)
print('O custo anterior era de')
print(f'R${CustoAntigo:,.2f}')
print('-' * 120)
print('Sendo assim ouve um aumento de')
print(f'R${Aumento:,.2f}')
print('=' * 120)