# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 02/12/2024
# Métodos para SET {}: clear(): Remove todos os elementos do set.

import os


os.system('cls')

# Titulo
print('-'*50)
print('Testando clear no set! c:\n Roupas pra lavar :0')
print('-'*50)

# Set
roupas = {'Casaco verde', 'Blusas uniforme', 'Calça preta'}

# Primeira saída
print(f'Roupas pra lavar: {roupas}')

# Uso do clear
roupas.clear()

# Saída Final
print('.'*50)
print(f'Roupas pra lavar: {roupas}')