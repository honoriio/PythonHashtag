lista = [1,2,3,4]
iteravel = iter(lista)
objeto_iteravel = iter(iteravel)
# Loop infinito
while True:
    try:
        # obtém o novo item
        elemento = next(objeto_iteravel)
        # faz algo com o elemento
    except StopIteration:
    # Se o StopIteration ocorrer, break no loop
        break