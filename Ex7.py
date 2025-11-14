seq1 = input("Digite a primeira sequência (ex: 1 0 1): ").split()
seq2 = input("Digite a segunda sequência: ").split()

cont = 0
n = len(seq1)
m = len(seq2)

for i in range(m - n + 1):
    if seq2[i:i+n] == seq1:
        cont += 1

print("Resultado:", cont)
