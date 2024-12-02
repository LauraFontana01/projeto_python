# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 02/12/2024
# Métodos para SET {}: difference(set2) ou -: Retorna um novo set com
# os elementos do primeiro set que não estão no segundo set.

import os


os.system('cls')

# Título
print('-'*50)
print('Testanto o método difference no set! c:\n')
print('-'*50)

# Set
set_1 = {'Lady Gaga', 'The Script', 'Stromae', 'Katy Perry'}
set_2 = {'New Order', 'Foo Fighters', 'Lady Gaga', 'Stromae'}

# Saída principal
print(f'Meus CDs: {set_1}')
print('.'*50)
print(f'CDs preferidos: {set_2}')

# hm...ainda vou preencher com o que eu entendi
meuscds = set_1.difference(set_2)

print('-'*50)
print(f'CDs que estão nas duas listas: {meuscds}')