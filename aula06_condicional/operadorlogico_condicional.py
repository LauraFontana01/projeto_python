# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 29/10/2024
# Estudo de Condicionais: Parte 4
# Operadores Lógicos

import os


os.system('cls')

# Declaração
a = 10
b = 5
c = 'John'

print('-'*50)
print(' Condicionais: Operadores Lógicos')
print('-'*50)

# E (and) VERDADEIRO
print('E (and) VERDADEIRO')
if (a > 5 and b != c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')

print ('-'*50)

# E (and) FALSO
print('E (and) FALSO')
if(a > 5 and b == c):
   print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')

print('-'*50)

# OU (or) VERDADEIRO
print('OU (or) VERDADEIRO')
if (a > 5 or b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')

print('-'*50)

# OU (or) FALSO
print('OU (or) FALSO')
if (a < 5 or c == 'Jane'):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
print('-'*50)
print()