n = int(input("Ingrese un número entero positivo: "))

if n < 0:
    print("Numero invalido")
else:
    factorial = 1
    contador = 1
    while contador <= n:
        factorial = factorial * contador
        contador = contador + 1
    print(f"El factorial de {n} es {factorial}")