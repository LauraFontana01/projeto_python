# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# G) Faça um programa que sorteia os números da Mega Sena e da Lotofácil

import os
import random


os.system('cls')

# Título
print('=' * 90)
print('Simulador de sorteio da Mega Sena e Lotofácil:')
print('=' * 90)
print()

# Entrada
mega_sena = random.sample(range(1, 61), 6)
lotofacil = random.sample(range(1, 26), 15)

# Ordenação em lista
mega_sena.sort()
lotofacil.sort()

# Saída
print('=' * 90)
print(f'Números sorteados Mega Sena: {mega_sena}')
print('-' * 90)
print(f'Números sorteados Lotofácil: {lotofacil}')
print('=' * 90)
print()
