a = list(map(int, input("Digite a primeira sequência ordenada: ").split()))
b = list(map(int, input("Digite a segunda sequência ordenada: ").split()))
resultado = []
i = j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        resultado.append(a[i])
        i += 1
    elif b[j] < a[i]:
        resultado.append(b[j])
        j += 1
    else:
        resultado.append(a[i])
        resultado.append(b[j])
        i += 1
        j += 1
while i < len(a):
    resultado.append(a[i])
    i += 1
while j < len(b):
    resultado.append(b[j])
    j += 1
print(resultado)
