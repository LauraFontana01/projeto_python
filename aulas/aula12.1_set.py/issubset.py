# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 02/12/2024
# Métodos para SET {}: issubset(set2): Verifica se o set é um 
# subconjunto de outro set.

import os


os.system('cls')

print('-'*50)
print('Testando o método Is Subset (issubset) no set! c:\n')
print('-'*50)

# Set
a = {1, 2}
b = {1, 2, 3, 4}
print(f'Lista 1: {a}')
print('.'*50)
print(f'Lista 2: {b}')
print('-'*50)
print('A Lista A está presente na lista B?')
print(a.issubset(b))  # Saída: True

