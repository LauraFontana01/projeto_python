# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Função Void - 
# A cachorrinha Lulu casou com o cachorro Pepe Lisboa. Qual o novo sobrenome da Lulu?
import os


os.system('cls')


# Função
def casar(nome, sobrenome):
    casamento = nome + sobrenome
    print(f'O novo nome da lulu é {casamento}')
  
# Programa Principal 
nome = 'Lulu'
sobrenome = 'Lisboa'
novo_nome = casar(nome, sobrenome)

