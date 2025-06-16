n = int(input("Ingrese un numero entre 2 y 50: "))

if n < 2 or n > 50:
    print("El numero debe estar entre 2 y 50.")
else:
    print(f"Los divisores de {n} son:")
    i = 1
    while i <= n:
        if n % i == 0:
            print(i)
        i += 1