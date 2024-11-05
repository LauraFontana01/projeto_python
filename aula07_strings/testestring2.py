# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 05/11/2024
# String em Python

import os


os.system('cls')

print('-'*50)
print('Funções String')
print('-'*50)

frase1 = "Olá, Mundo!"
quantidade_caracteres = len(frase1) # Conta os caracteres
print(f'A frase {frase1} \ncontém {quantidade_caracteres} caracteres')
print('.'*50)

minusculas = frase1.lower() # Frase em minúsculo
print(f'Frase original: {frase1}')
print(f'Frase nova: {minusculas}')
print('.'*50)

capitalizada = frase1.capitalize # Frase capitalizada
print(f'Frase original: {frase1}')
print(f'Frase nova: {capitalizada}')
print('.'*50)

frase2 = '    Olá, Mundo!    '
sem_espacos = frase2.strip() # Retirar espaços, antes e depois
print(f'Frase original: {frase2}')
print(f'Frase nova: {sem_espacos}')
print('.'*50)

substituicao = frase1.replace("Mundo", "Python") # Troca Palavra
print(f'Frase original: {frase1}')
print(f'Frase nova: {substituicao}')
print('.'*50)

lista = frase1.split (",") # Separa as palavras de uma str em uma lista
print(f'Frase original: {frase1}')
print(f'Frase nova: {lista}')
print('.'*50)

lista = ['Olá, Mundo!']
juncao = "-".join(lista) # Transforma uma lista em uma string com separador
print(f'Frase original: {lista}')
print(f'Frase nova: {juncao}')
print('.'*50)

# upper ou lower = maiusulo e minusculo