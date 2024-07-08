import random
pessoas = []
pessoa = {}

while True:
    nome = input('Nome: ')
    idade = input('Idade: ')
    cidade = input('Cidade: ')

    ids = random.randint(100000, 999999)

    pessoa.update({'id': ids, 'Nome': nome, 'Idade': idade, 'Cidade': cidade})
    pessoas.append(pessoa)

    print('-' * 60)
    resposta = input('Deseja contiuar?: ').upper()
    if resposta == 'NÃO' or resposta == 'NAO':
        break
    else:
        pass

for chave in pessoas:
    print(f'Nome: {chave}')