dicionario = {}
lixeira = {}
lista = []

nome = input('Nome: ')

dicionario.update({'Nome': nome})

print(dicionario)


delet = dicionario.pop('Nome')

print(dicionario)

if delet != "":
    lixeira.update({'Nome': delet})
    print(dicionario)
    print(lixeira)
else:
    print('Não a nada na variavel delet')



# Aqui foi testado uma forma de criar uma lixeira, onde, um item foi excluido de um dicionario e foi adicionado a lixeira, onde eu posso pedir para restaurar esse item para o meu dicionario
# Pincipal depois, vou testar isso no app de agenda de contatos depois. 
# No caso, eu posso deixar a escolha de exclusão para o usuario e tambem deixar na mão do mesmo a opção de ver o que foi excluido e se o mesmo quer restaurar isso para a agenda mestre 