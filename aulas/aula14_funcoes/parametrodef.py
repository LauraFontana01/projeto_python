# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 20/01/2025

import os


os.system('cls')

# Definindo a função
def dados_paciente(nome='Laura', nascimento=2001, peso=40, altura=1.45):
    print(f'Bem-vindo(a) ao sistema Senac, {nome}!')
    print(f'O ano de nascimento de/da {nome} é {nascimento}.')
    print(f'O peso de/da {nome} é {peso}kg.')
    print(f'A altura de/da {nome} é {altura}m.')
    print('-'*50)

# Inicio Para Lembrar
def posicional_nomeado(nascimento, nome='Laura',): #Ok, funciona!
    print(f'Bem-vindo(a) ao sistema Senac, {nome}!')
    print(f'O ano de nascimento de/da {nome} é {nascimento}.')
    print('-'*50)


# Invocando a função
dados_paciente()

dados_paciente(nome='Bruno', nascimento=1999, peso=71, altura=1.78)
dados_paciente(nascimento=2001, nome='Flaura', peso=40, altura=1.45)
dados_paciente(altura=1.45, peso=40, nome='Lauritos', nascimento=2001)