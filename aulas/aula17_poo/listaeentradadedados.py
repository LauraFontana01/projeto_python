# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 11/02/2024

import os
from cadastro import cadastrar_estudante
from resultados import exibir_resultados


def main():
    os.system('cls')
    print('Cadastro de Alunos')
    print('-'*70)

    # Lista para armazenar os estudantes cadastrados
    estudantes = []

    while True:
        # Chama a função para cadastrar um novo estudante
        estudante = cadastrar_estudante()
        estudantes.append(estudante)

        continuar = input('Deseja cadastrar outro estudante? (s/n): ')
        if continuar != 's':
            break # perguntar pro bruno a importancia do break

        # Exibe os resultados de todos os estudanres cadastrados
        exibir_resultados(estudantes)

    # Bloco que garante que a função main() só será executada
    # quando o arquivo for executado diretamente e não quando for importado como módulo
    if __name__ == "__main__":
        main()