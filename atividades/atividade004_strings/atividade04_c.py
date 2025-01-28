# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 05/11/2024
# String em Python
# Faça um programa que leia o nome de uma pessoa e verifique se a palavra 'Oliveira' está presente neste nome, mostrando True ou False.

import os


os.system('cls')

nome = input('Digite seu nome completo: ')

print(f'Nome: {nome}')
if "Oliveira" in nome:
    print('Você é da família Oliveira!')
else:
    print('Você não tem o sobrenome "Oliveira"!')
