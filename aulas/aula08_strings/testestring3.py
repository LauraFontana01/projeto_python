# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 05/11/2024
# String em Python

import os


os.system('cls')

print('.'*50)
print('Operadores úteis para')
print('Strings e Estruturas de Dados')
print('~'*50)

texto = "Olá, Mundo!"

print(f'Texto: {texto}')
if "Mundo" in texto: #Verifica a palavra dentro da String
    print('A palavra "Mundo" está presente na string.')
else: 
    print('A paavra "Mundo" não está present na string.')

print('~'*50)

texto2 = "Olá, Python!"

print(f'Texto: {texto2}')
if "Mundo" not in texto2: # Verifica a palavra dentro da string
    print('A palavra "Mundo" não está presente na string')
else:
    print('A palavra "Mundo" está presente na string.')

print('.'*50)