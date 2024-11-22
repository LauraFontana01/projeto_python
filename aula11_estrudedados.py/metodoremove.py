# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Estrutura de Dados
#O código exibe uma lista inicial, permite que o usuário remova um elemento especificado (se existir na lista) e mostra a lista atualizada ou uma mensagem de erro caso
#  o elemento não seja encontrado.



import os


os.system('cls')

# Lista original
lista = [1, 2, 3, 4]

# Mostrando a lista original
print('Lista original:', lista)

# Pedindo o usuário o elemento a ser removido
elemento = input('Elemento a ser removido: ')

# Tentando remover o elemento da lista
if elemento.isdigit():
    elemento = int(elemento)  # Converte para inteiro se for um número
if elemento in lista:
    lista.remove(elemento)
    print('Lista após a remoção:', lista)
else:
    print('Elemento não encontrado na lista.')