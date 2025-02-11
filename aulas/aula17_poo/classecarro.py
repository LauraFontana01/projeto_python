# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 11/02/2024
# Diferença entre: parametro (&) recebe valor padrão default e arguento ($) recebe valor real (valor inserido pelo usuario ou já definido; iteração)

import os


class Veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor


# Solicitando entrada de dados do usuário
os.system('cls')
print('-'*70)
marca = input('Digite a marca do veículo: ')
modelo = input('Digite o modelo do veículo: ')
ano = int(input('Digite o ano do veículo: '))
cor = input('Digite a cor do veículo: ')

# Criando um objeto da classe Veiculo com os dados fornecidos pelo usuário
veiculo1 = Veiculo(marca, modelo, ano, cor)

# Acessando e imprimindo atributos do objeto 
print('-'*70)
print('\nInformações do Veículo: ')
print('-'*70)
print(f'Marca: {veiculo1.marca}')
print(f'Modelo: {veiculo1.modelo}')
print(f'Ano: {veiculo1.ano}')
print(f'Cor: {veiculo1.cor}')
print('-'*70)