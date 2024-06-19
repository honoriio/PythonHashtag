'''6. Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:

a. O modelo do carro mais econômico;
b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará,
 considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo.
 Os dados são fictícios e podem mudar a cada execução do programa.'''


veiculos = ['fusca',' gol', 'uno', 'vectra', 'peugeot']
autonomias = [7, 10, 12.5, 9, 14.5]

autonomia = []
custo = []

print('=' * 80)
print('COMPARATIVO DE AUTONOMIA'.center(80))
print('=' * 80)

for i, veiculo in enumerate(veiculos):
    litros = (1000 / autonomias[i])
    custo_km = (litros * 2.25)
    autonomia.append(litros)
    custo.append(custo_km)
    print(f'Modelo: {veiculo} - KM/Litro: {autonomias[i]:.2f} - Litros Gasto: {autonomia[i]:.2f} - Custo Total: R${custo[i]:,.2f}')
    
menor_consumo = max(autonomias)
indice = autonomias.index(menor_consumo)

print(f'O Modelo de menor consumo é {veiculos[indice]}')