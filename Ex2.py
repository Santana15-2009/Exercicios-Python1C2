tipo = input("Digite F para Fahrenheit ou C para Celsius: ")
temp = float(input("Digite a temperatura: "))
if tipo == "F":
    print("Celsius:", (temp - 32) * 5 / 9)
elif tipo == "C":
    print("Fahrenheit:", (temp * 9 / 5) + 32)
