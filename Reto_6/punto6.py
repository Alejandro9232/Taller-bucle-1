def es_primo(n):
    if n < 2:
        return False
    divisor = 2
    while divisor <= n // 2:
        if n % divisor == 0:
            return False
        divisor += 1
    return True

def mostrar_primos_hasta_100():
    print("Números primos del 1 al 100:")
    numero = 1
    while numero <= 100:
        if es_primo(numero):
            print(numero)
        numero += 1

mostrar_primos_hasta_100()