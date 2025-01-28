# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 02/12/2024
# Métodos para SET {}: intersection(set2) ou &: Retorna um novo set
# que é a interseção de dois sets. intersecao = set_1.intersection(set_2) ou "print(set_1 & set_2)"

import os


os.system('cls')

#Título
print('-'*50)
print('Testando o método Intersection no set! c:\n ')

# Sets
set_1 = {2, 4, 6}
set_2 = {4, 8, 12}
set_3 = {'Duna', 'Tapas e Beijos', 'Stranger Things'}
set_4 = {'Tapas e Beijos', 'Avenida Brasil', 'Os Suburbanos'}

# Interseção dos sets
intersecao_1 = set_1.intersection(set_2)
intersecao_2 = set_3.intersection(set_4)

# Saída Inicial
print('-' * 50)
print(f'Set 1: {set_1}')
print('.' * 50)
print(f'Set 2: {set_2}')
print('.' * 50)
print(f'Set 3: {set_3}')
print('.' * 50)
print(f'Set 4: {set_4}')
print('-' * 50)
print()
print('-' * 50)
print(f'Interseção Set 1 e Set 2: {intersecao_1}')
print('.' * 50)
print(f'Interseção Set 3 e Set 4: {intersecao_2}')
print('-' * 50)
print()