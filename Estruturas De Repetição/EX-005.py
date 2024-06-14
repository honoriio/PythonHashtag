quarto = []


while True:
    nome = input('INFORME O NOME DO HOSPEDE: ')
    cpf = input('INFORME O CPF DO HOSPEDE: ')
    resposta = input('DESEJA CONTINUAR: [SIM]/[NÃO]: ').upper()
    pessoa = [nome, cpf]
    quarto.append(pessoa)
    if resposta == 'NAO' or resposta == 'NÃO':
        break

print('=' * 120)
print('PESSOAS HOSPEDADAS'.center(120))
print('=' * 120)
for pessoa in quarto:
    print(pessoa)