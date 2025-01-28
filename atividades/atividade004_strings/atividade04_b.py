# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 05/11/2024
# String em Python
# Faça um programa que receba o nome 'João da Silva' e, em seguida, substitua 'Silva' por 'Oliveira'.

import os


os.system('cls')

frase1 = 'João da Silva'
substituicao = frase1.replace("da Silva", "de Oliveira")

print(f'Nome original: {frase1}')
print(f'Nome com Substituição: {substituicao}')