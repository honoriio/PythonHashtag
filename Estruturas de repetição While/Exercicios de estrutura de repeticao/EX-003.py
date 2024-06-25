'''3. Faça um programa que leia e valide as seguintes informações (e para cada uma delas, continue pedindo a informação até o usuário inserir corretamente):
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'''

nome = input('Informe seu nome: ')
while len(nome) < 4:
    print('Informe um nome com mais de 3 caracteres.')
    nome = input('Informe seu nome: ')

idade = int(input('Informe sua idade: '))

while not (1 <= idade <= 150):
    print('Informe a idade que seja maior que 0 e menor que 150')
    idade = int(input('Informe a idade: '))

salario = float(input('Informe seu salario R$: '))

while salario <= 0:
    print('Informe um salario maior que 0')
    salario = float(input('Informe seu salario R$: '))

genero = input('Informe seu sexo: ')

while not genero in ['f', 'm']:
    print('Informe seu genero corretamente')
    genero = input('Genero: ')

estado_civil = input('Informe seu estado civil: ')

while not estado_civil in ['s', 'c', 'v', 'd']:
    print('Informe um estado civil correto.')
    estado_civil = input('Informe seu estado civil: ')

pessoas = []

pessoas.append([nome, idade, salario, genero, estado_civil])

for pessoa in pessoas:
    print(f'Nome: {pessoa[0]}, Idade: {pessoa[1]}, salario: R${pessoa[2]}, Genero: {pessoa[3]}, Estado Civil: {pessoa[4]}')