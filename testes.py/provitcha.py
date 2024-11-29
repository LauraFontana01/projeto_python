import os


os.system('cls')


lista = ['Amo luzes verdes', 'Poneis coloridos', 'Lauras Felizes', 'Dexter gostosinho de mamãe']

lista_ordenada= sorted(lista) # coloca em ordem alfabetica

lista_desordenada = sorted(lista, reverse = True) # inverso

lista.append('Jubileias Coloridas') # add coisinhas

lista.insert(4, 'Salsa Fogosa') # insere algo em um indice especifico


print(lista)
print(lista_ordenada)