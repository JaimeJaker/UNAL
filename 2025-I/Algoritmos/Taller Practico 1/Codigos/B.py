"""
Author: jangulot
Complejidad memoria: O(1) - Solo se generan combinaciones de 3 letras a la vez.
Complejidad tiempo: O(26^3) - En el peor caso, prueba todas combinaciones de 3 letras.
"""

from itertools import product

def numero_a_cadena(n):
    letras = [chr(i) for i in range(ord('a'), ord('z') + 1)]  # O(26) M(26)

    for p in product(letras, repeat=3):  # O(26^3) M(1)
        if sum(ord(c) - ord('a') + 1 for c in p) == n:  # O(3) M(1)
            return ''.join(p)  # O(1) M(1)

    return None  # O(1) M(1)

# Lectura de entrada
casos_prueba = int(input())  # O(1) M(1)

for _ in range(casos_prueba):  # O(t) M(1)
    numero = int(input())  # O(1) M(1)
    resultado = numero_a_cadena(numero)
    print(resultado)  # O(1) M(1)