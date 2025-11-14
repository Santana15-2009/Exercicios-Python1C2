def e_primo(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input("Digite um número: "))

menor = n
while menor >= 2 and not e_primo(menor):
    menor -= 1

maior = n
while not e_primo(maior):
    maior += 1

