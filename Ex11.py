vetor = []
for i in range(8):
    vetor.append(int(input("Digite um número: ")))
positivos = []
negativos = []
for i in vetor:
    if i > 0:
        positivos.append(i)
    elif i < 0:
        negativos.append(i)
print("Positivos:", positivos)
print("Negativos:", negativos)
