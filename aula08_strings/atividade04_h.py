# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 05/11/2024
# String em Python
# Faça um programa que leia o nome de um aluno e mostre quantas vezes a letra 'o' aparece e em que posição ela aparece pela primeira e última vez.
# find(substring): retorna o índice da primeira ocorrência da substring na string. Se a substring não for encontrada, retorna -1. (serve para validação, se voltar -1 é porque tem um problema)

import os


os.system('cls')

print('~'*50)
print('Contagem e localização da letra "O"')
print('.'*50)

frase = input('Digite o nome do aluno: ').lower()

contagem_os = frase.count('o')
primeiro_o = frase.find('o') 
ultimo_o = frase.rfind('o')

print('~'*50)
print(f'A letra "O" aparece {contagem_os} vez/vezes!')
print(f'No índice, aparece em {primeiro_o} e por último em {ultimo_o}')
print('.'*50)


