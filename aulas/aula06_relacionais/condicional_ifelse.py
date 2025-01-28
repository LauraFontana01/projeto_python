# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 29/10/2024

import os

os.system('cls')

# Declaração de Variaveis
a = 10
b = 5
c = 'José'
d = 'José'

print('-'*50)
print('Condicionais: Operadores Relacionais')
print('-'*50)

# Operador de Igualdade (==)
if c == d:
    print('-'*50)
    print(f'{c} é igual {d}')
    print('-'*50)
else:
    print(f'{c} não é igual a {d}')

# Operador de Diferença (!=)
if a != c:
    print('-'*50)
    print(f'{a} é diferente de {c}')
    print('-'*50)
else:
    print(f'{a} não é diferente de {c}')

# Operador de Maior que (>)
if a > b:
    print('-'*50)
    print(f' {a} é maior que {b}')
    print('-'*50)
else:
    print(f'{a} não é maior que {b}')

# Operador de Menor que (<)
if b < a:
    print('-'*50)
    print(f'{b} é menor que {a}')
    print('-'*50)
else:
    print(f'{b} não é menor que {b}')

# Operador de Maior ou igual a (>=)
if a >= b:
    print('-'*50)
    print(f'{a} é maior ou igual a {b}')
    print('-'*50)
else: print(f'{a} não é maior ou igual a {b}')

# Operador de Menor ou igual a (<=)
if b <= a:
    print('-'*50)
    print(f'{b} é menor ou igual a {a}')
    print('-'*50)
else:
    print(f'{b} não é menor ou igual a {a}')

print('Fim do programa!')
print('-'*50)
print()