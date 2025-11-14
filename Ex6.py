def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat

soma = 0

for i in range(1, 6):
    num = int(input(f"Digite o {i}º número inteiro: "))
    soma += fatorial(num)

print(f"\nA soma dos fatoriais é: {soma}")

