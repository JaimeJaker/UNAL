"""
    author: jangulot
    complejidad tiempo: O(n log S)
    complejidad memoria: O(n)
    donde:
      - n es el número de casilleros (longitud de la lista t),
      - S es la suma total de basura (sum(t)).
    Algoritmo: Búsqueda binaria sobre la cantidad mínima de trabajadores m
    tal que es posible limpiar la calle según las reglas del problema.
"""

import sys  # O(1) M(1)
input = sys.stdin.readline  # O(1) M(1)

def es_factible(t, m):  # O(n) M(1)
    carry = 0  # O(1)
    n = len(t)  # O(1)

    for i in range(n):  # O(n)
        total = t[i] + carry  # O(1)
        if total <= m:  # O(1)
            carry = 0  # O(1)
        else:
            if i == n - 1:  # O(1)
                return False  # O(1)
            if total > 2 * m:  # O(1)
                return False  # O(1)
            moves = total - m  # O(1)
            carry = 2 * moves  # O(1)
    return True  # O(1)

def main():  # O(n log S) M(n)
    n = int(input().strip())  # O(1) M(1)
    t = list(map(int, input().split()))  # O(n) M(n)
    
    lo, hi = 0, sum(t)  # O(n) M(1)
    respuesta = hi  # O(1)

    while lo <= hi:  # O(log S)
        mid = (lo + hi) // 2  # O(1)

        if mid == 0:  # O(1)
            if all(x == 0 for x in t):  # O(n)
                print(0)  # O(1)
                return  # O(1)
            else:
                lo = 1  # O(1)
                continue  # O(1)

        if es_factible(t, mid):  # O(n)
            respuesta = mid  # O(1)
            hi = mid - 1  # O(1)
        else:
            lo = mid + 1  # O(1)

    print(respuesta)  # O(1)

if __name__ == "__main__":  # O(1)
    main()  # O(n log S) M(n)
