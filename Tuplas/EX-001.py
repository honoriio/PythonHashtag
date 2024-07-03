'''1. Análise de Vendas
Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.

Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam.'''


meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]

for item in vendas:  # Aqui o item se torna uma tupla, pegando o valor de cada umas das tuplas que estão armazendas em vendas
    nome, valor = item # aqui acontece a desconpactação das tuplas, sendo assim passando os valores para as variaveis. 
    if valor >= meta: # Condição para mostrar apenas os vendedores que conseguiram bater a meta
        print(f'O vendedores que bateram a meta foi {nome} com o valor de R${valor:,.2f}')

# No final acaba sendo mais facil trabalhar com a tupla, nessa forma do que com a lista, para tratamentos de dados se torna melhor. 
