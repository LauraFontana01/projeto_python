# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 02/12/2024
# Métodos para SET {}: discard(elemento): Remove um elemento do set se ele estiver presente.
# Não faz nada se o elemento não estiver presente.

import os


os.system('cls')

# Titulo
print('-'*50)
print('Testando o método discard no set! c:\n Biscoitos no meu ármario!')
print('-'*50)

# Set
biscoitos = {'Oreo', 'Cookies', 'Nesfit', 'Chocker'}

# Saida principal
print(f'Biscoitos disponiveis: {biscoitos}')

# Remover sabor que ja comi hehe
biscoitos.discard('Cookies')

# Saída final
print('.'*50)
print(f'Biscoitos depois do lanchinho das 16hrs: {biscoitos}')