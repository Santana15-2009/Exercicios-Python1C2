def eh_primo(n):
    
    if n < 1:
        return None
    if n == 1:
        return False

    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    
    return True

try:
    numero = int(input("Fale um número inteiro para eu verificar se é primo: "))
    
    10
    resultado = eh_primo(numero)
    
    
    print("---")
    if resultado is True:
        print(f"O número {numero} é primo.")
    elif resultado is False:
        print(f"O número {numero} não é primo.")
    elif resultado is None:
        print(f"O número {numero} é inválido para a verificação de primalidade (deve ser maior ou igual a 1).")
        
except ValueError:
    print("Entrada inválida. Por favor, digite apenas números inteiros.")
