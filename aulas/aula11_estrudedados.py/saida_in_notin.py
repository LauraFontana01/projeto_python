# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Estrutura de Dados
# O código verifica se um número está presente em uma lista usando in e, caso afirmativo, exibe sua posição; caso contrário, informa que o número não está na lista. 
# Em seguida, verifica se um nome não está presente em outra lista usando not in, adiciona o nome à lista se ele não estiver presente e exibe a lista antes e depois da adição.
import os


os.system('cls')

print('-'*50)
print(' Saida com In e Not In ')
print('-'*50)

# Exemplo com In
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if (3 in lista_numeros):
    print(lista_numeros)
    posicao = lista_numeros.index(3)
    print(f'O número 3 está na posição {posicao}')
else:
    print('O elemento não consta na listagem')

print()
print('-'*50)
# Exemplo com Not In
lista_nomes = ['Kate', 'Lily', 'Chloé']

if ('Kristen' not in lista_nomes):
    # Antes
    print(lista_nomes)

    # Não está na lista, acrescentar
    lista_nomes.append('Kristen')

    print('\nO nome Kristen foi acrescentado!')
    print(lista_nomes)

print()
print('-'*50)
print('Fim do programa!')
print('-'*50)