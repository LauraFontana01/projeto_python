# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 24/10/2024

import os

os.system('cls')

print('-'*70)
print('Operadores Aritméticos: Ordem de Precedência')
print('-'*70)

# Entrada
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
nota4 = float(input('4°ª nota: '))         

# Processamento
soma = nota1 + nota2 + nota3 + nota4
media = nota1 + nota2 + nota3 + nota4 / 4
media_correta = (nota1 + nota2 + nota3 + nota4) / 4 

# Saída
print('---- Notas ---------------')
print(f'Nota 1: {nota1} | Nota 2: {nota2}| '
      f'Nota 3: {nota3} | Nota 4: {nota4}')
print('-'*70)
print(f'Media errada: {media}')
print(f'Média correta: {media_correta}')
print('-'*70)