# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 18/11/2024
# Estrutura de Repetição

# Faça um programa que imprima os números primos entre 0 e 100.

import os


os.system('cls')

print('-'*50)
print('Números primos')
print('.'*50)

# Looping (1) entre 0 a 100
for numero in range(0, 101):
    # Condição onde 0 e 1 são eliminados pois não são números primos, ou seja, divisiveis por 1 ou por ele mesmo
    if numero < 2:
        continue # Continua o looping
    # Condição para os números de 2 a 100
    else: 
        # Validação (2) para nº primo
        primo = True

        for divisor in range(2, int(numero ** 0.5) + 1):
            if numero % divisor == 0:
                primo = False
        if primo:
        # Saída
            print(f'{numero}')