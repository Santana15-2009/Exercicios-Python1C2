def eh_bissexto(ano):
    """
    Verifica se um ano é bissexto.
    Um ano é bissexto se:
    1. É múltiplo de 400. OU
    2. É múltiplo de 4 E não é múltiplo de 100.
    """
 
    if ano % 400 == 0:
        return True
   
    elif (ano % 4 == 0) and (ano % 100 != 0):
        return True

    else:
        return False



try:
  
    ano = int(input("Digite um ano (valor inteiro): "))
    
 
    if eh_bissexto(ano):
        print(f"O ano {ano} é BISSEXTO.")
    else:
        print(f"O ano {ano} NÃO é bissexto.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro válido.")
