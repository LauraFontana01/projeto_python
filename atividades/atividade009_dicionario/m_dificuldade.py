# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 16/01/2025
# Desenvolva um programa para gerenciar viagens de uma empresa de turismo.
# Ele deve: Cadastrar no mínimo 5 viagens com destino, data de partida, 
# duração e número de vagas disponíveis.
# Permitir alterar dados das viagens.
# Listar todas as viagens cadastradas, organizadas por destino.
# Gerar um relatório com:
# Quantas viagens têm menos de 10 vagas disponíveis.
# Quantas ocorrerão depois de 01/06/2025.

import os


os.system('cls')

viagens = {}


while True:
    print('1. Alterar dado de uma viagem.')
    print('2. relatório.')
    print('3. Sair.')

    opcao = input('Escolha alguma opção: ')