import time
print("Los numeros impares del 1 al 1000")

a = 1

while a <= 1000:
	print(a)
	a += 2
	time.sleep(0.05)
	
print("Los numeros pares del 1 al 1000")

b = 2

while b <= 1000:
	print(b)
	b += 2
	time.sleep(0.05)
print("fin")