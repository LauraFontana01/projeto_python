# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 20/01/2025

import os

# definição da função
def multiplicar(a, b=1):
    return a * b


os.system('cls')

resultado_1 = multiplicar(5)
resultado_2 = multiplicar(5, 2)

print(f'Primeiro resultado: {resultado_1}')
print(f'Segundo resultado: {resultado_2}')
print()