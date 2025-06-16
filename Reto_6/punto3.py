import time
n = int(input("Ingrese un número entero: "))

if n % 2 != 0:
    n -= 1

while n >= 2:
    print(n)
    n -= 2
    time.sleep(0.01)
print("finalizado")