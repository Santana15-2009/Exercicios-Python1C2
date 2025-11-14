a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Digite o operador (+, -, *, /): ")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Divisão por zero")
