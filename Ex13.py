def media(v):
    soma = 0
    for numero in v:
        soma += numero
    return soma / len(v)

entrada = input("Digite os números separados por espaço: ")
v = [float(x) for x in entrada.split()]

print("Média =", media(v))
