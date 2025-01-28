# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# D) Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.

print('-'*50)
print('Média de notas')
print('-'*50)

notas = []
soma = 0

for i in range(1, 5):
    nota = float(input(f'Digite a nota do aluno {i}: '))
    notas.append(nota)
print('-'*50)

for nota in notas:
    soma += nota
    
    media = soma / 4

print(f'A soma das notas é: {soma}')
print(f'A média das notas é: {media}')
print('-'*50)
    



