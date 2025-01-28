# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# G) Ler uma lista com 10 números, depois apresente o maior e o menor número da lista

import os


os.system('cls')

minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

maior_numero = max(minha_lista)
menor_numero = min(minha_lista)

print(f'Minha Lista: {minha_lista}')
print(f'Maior Número: {maior_numero}')
print(f'Menor Número: {menor_numero}')