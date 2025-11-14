n = int(input("Digite o tamanho da série de Fibonacci: "))
a, b = 0, 1
lista = []
for i in range(n):
    lista.append(a)
    a, b = b, a + b
print(lista)
