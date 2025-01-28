def dividir(a, b):
    # Método para dividir 2 números

    # Args:
    #   a (any): dividendo
    #   b (any): divisor

    # Returns:
    #   str: Mensagem de erro ou 'Ok!' se a divisão for bem-sucedida
    #   any: quociente ou none em caso de erro

   if b == 0:
      return None, 'Erro de divisão'
   else:
      divisao = a / b
      return divisao, 'Ok!'