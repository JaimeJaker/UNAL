"""
author: jangulot
complejidad tiempo: O(q * log n)
complejidad memoria: O(n)
"""

def busqueda_binaria(arreglo, elemento):  # O(log n) M(1)
    izquierda = 0                  # O(1) M(1)
    derecha = len(arreglo) - 1    # O(1) M(1)
    resultado = -1                # O(1) M(1)
    while izquierda <= derecha:   # O(log n) M(1)
        medio = (izquierda + derecha) // 2  # O(1) M(1)
        if arreglo[medio] == elemento:      # O(1) M(1)
            resultado = medio               # O(1) M(1)
            derecha = medio - 1             # O(1) M(1)
        elif arreglo[medio] < elemento:     # O(1) M(1)
            izquierda = medio + 1           # O(1) M(1)
        else:
            derecha = medio - 1             # O(1) M(1)
    return resultado                        # O(1) M(1)

n, q = map(int, input().split())           # O(1) M(1)
arreglo = list(map(int, input().split()))  # O(n) M(n)

for i in range(q):                          # O(q * log n) M(1)
    elemento = int(input())                # O(1) M(1)
    print(busqueda_binaria(arreglo, elemento))  # O(log n) M(1)
