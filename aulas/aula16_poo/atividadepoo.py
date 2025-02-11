# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 11/02/2024
# Refazendo a Atividade A 004 com Orientação a Objeto

import os


def limpeza_terminal():
    os.system('cls')

def titulo():
    print('-'*80)
    print('Vamos descobrir o seu nome!'.center(80))
    print('-'*80)
    print()

class Nome:
    def __init__(self, nome, nomedomeio, sobrenome,): # init(método construtor) sempre tera dois underlines       metodo construtor()
        self.nome = nome
        self.nomedomeio = nomedomeio
        self.sobrenome = sobrenome

# Iniciação do sistema
limpeza_terminal()
titulo()

# Solicitando entrada de dados ao usuário
print('-'*80)
nome = input('Digite seu nome: ').capitalize()
nomedomeio = input('Digite seu nome do meio: ').capitalize()
sobrenome = input('Digite seu sobrenome: ').capitalize()

# Variavel que une três variaveis de strings
nomecompleto = nome + ' ' + nomedomeio +' ' + sobrenome

# Criando um objeto de classe Nome com os dados fornecidos pelo usuario
nome1 = Nome(nome, nomedomeio, sobrenome)

print('-'*80)
print(f'Vimos aqui que seu nome completo é {nomecompleto}! Um nome belo e forte, parabéns! :)')
