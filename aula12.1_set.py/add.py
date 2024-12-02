# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 02/12/2024
# Métodos para SET {}: add(elemento) Adiciona um elemento ao set.

import os


os.system('cls')

# Entrada do título
print('-'*50)
print('Testando o elemento add no set! c:\n Escolinha de Pets da Tia Lau - novos miaulunos')
print('-'*50)

# Set
alunos = {'Kiki', 'Olavo', 'Miausculo', 'Ester Ludamura', 'Billy'}

# Saída Inicial
print(f'Alunos até 29/11: {alunos}')
print('.'*50)

# Adicionou novo aluno
alunos.add('Bruno Miaudgers')
print(f'Alunos após dia 02/12: {alunos}')