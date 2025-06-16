import time

n = 1

while n <=100:
	print("numeros con respectivo cuadrado")
	cuadrado = n**2
	print(f"el numero {n} y su cuadrado {cuadrado}")
	time.sleep(0.2)
	n += 1
print("fin")