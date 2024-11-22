# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 04/11/2024
# Biblioteca Math
# Faça um programa onde o usuário tenta adivinhar o número que o computador está ‘pensando’.

import os
import random


os.system('cls')

print('.'*50)
print('MiniGame: Adivinhe qual número estou pensando!')
print('~'*50)

numero = int(input('Digite um número de 1 a 10: '))

sorteado = random.randint(1, 10)

if numero == sorteado:
    print('Parabéns! Você acertou! Você tem um ótimo feeling! c: ')
else:
    print(f'Vish, o número sorteado foi {sorteado}! Continue tentando! :p')

