# Melhorando o cadastro de cpf  fazendo o uso de strings



# Cogigo gerado pelo Copilote

cpf = input('Informe o seu CPF, sem os dígitos separadores: ')

if len(cpf) != 11 or not cpf.isdigit():
    print('Por favor, insira exatamente os 11 dígitos do seu CPF e certifique-se de que são todos números.')
else:
    print('CPF validado')



# Melhorando o cadastro de cpf  fazendo o uso de strings

# Codigo feito por mim, preciso verificar o mesmo depois e ver onde foi que errei

cpf = input('INforme o seu CPF, sem os digitos separadores: ')

digitos = len(cpf)

if digitos < 11:
    print('Por favor, insira os 11 digitos do seu CPF')
elif digitos > 11:
    print('Informe somente os 11 digitos do seu CPF')
    if cpf.isdigit():
        pass
    else:
        print('P or favor digite somente números.')
else:
    pass
    print('CPF validado')