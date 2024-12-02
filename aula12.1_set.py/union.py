# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 02/12/2024
# Métodos para SET {}: union(set2) ou |: 
# Retorna um novo set que é a união de dois sets. uniao = set_1.union(set_2) ou "print(set_1 | set_2)"

import os


os.system('cls')

# Titulo
print('-'*50)
print('Testando o método Union no set! c:\n Academia Fina Dança')
print('Comemoração dos alunos da Prof.Kauane e do Prof.Hugo')
print('-'*50)

# Sets
alunos_kauane = {'Livia', 'Zaya', 'George', 'Tassia', 'Gustavo'}
alunos_hugo = {'Deodara', 'Silvia', 'Laiane', 'Wilma', 'Barbara'}

# Saida Inicial
print(f'Alunos da Professora Kauane: {alunos_kauane}')
print('.'*50)
print(f'Alunos do Professor Hugo: {alunos_hugo}')

# União dos Sets
uniao_1 = alunos_kauane.union(alunos_hugo)

# Saída Final 
print('-'*50)
print(f'Alunos de ambos professores: {uniao_1}')
print('-'*50)
print('Agora é só organizar quem vai levar o que! c: Boas festas!')
