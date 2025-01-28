# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 16/01/2025
# Faça um programa para organizar eventos e participantes. Ele deve:
# Permitir o cadastro de eventos (nome, data e local) e associar participantes
# (nome e e-mail) a eles.
# Cadastrar no mínimo 3 eventos com participantes.
# Exibir a lista de eventos com seus participantes.
# Gerar um relatório com quantos eventos têm participantes
# associados e quantos ocorrerão depois de 01/01/2025.

import os


os.system('cls')

evento = {}

for i in range(1,2):
    nome = input('Insira o nome do evento: ').lower()
    nome_part = input('Nome participante: ')
    email = input('Email participante: ')
    data = input('Insira a data: ')
    localizacao =input('Insira a localização: ')

    evento[nome]