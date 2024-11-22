# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 25/10/2024

import os

import datetime

os.system('cls')

print('-'*70)
print('Eu consigo calcular sua idade!')
print('-'*70)

# Entrada com casting
nascimento = int(input('Ano de nascimento:'))

# Processamento: pegando o ano corrente
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento


# Saida interpolada
print(f'Você tem ou irá fazer {idade} anos! Tá ficando velhinho(a) hein? Já fez seu seguro de vida?')





