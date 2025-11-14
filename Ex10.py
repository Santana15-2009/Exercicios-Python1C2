lista = list(map(int, input("Digite os números da lista: ").split()))
c = int(input("Digite o valor de C: "))
achou = False
for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] * lista[j] == c:
            print("Resultado:", lista[i], "e", lista[j])
            achou = True
if not achou:
    print("Não existem tais números")
