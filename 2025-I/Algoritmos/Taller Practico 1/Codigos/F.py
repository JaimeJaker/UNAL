"""
author: jangulot
complejidad tiempo: O(Q * log N)
complejidad memoria: O(N + Q)
"""

def encontrar_ultima_ocurrencia(arr, x):  # O(log N) M(1)
    izquierda, derecha = 0, len(arr) - 1  # O(1) M(1)
    resultado = -1                        # O(1) M(1)
    while izquierda <= derecha:           # O(log N) M(1)
        medio = (izquierda + derecha) // 2  # O(1) M(1)
        if arr[medio] == x:               # O(1) M(1)
            resultado = medio             # O(1) M(1)
            izquierda = medio + 1         # sigue buscando hacia la derecha
        elif arr[medio] < x:              # O(1) M(1)
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return resultado                      # O(1) M(1)

if __name__ == "__main__":
    N, Q = map(int, input().split())           # O(1) M(1)
    elementos = list(map(int, input().split()))  # O(N) M(N)

    resultados_consultas = []                  # O(1) M(Q)
    for _ in range(Q):                         # O(Q * log N) M(1)
        consulta = int(input())                # O(1) M(1)
        indice = encontrar_ultima_ocurrencia(elementos, consulta)  # O(log N) M(1)
        resultados_consultas.append(indice)    # O(1) M(1)

    for res in resultados_consultas:           # O(Q) M(1)
        print(res)                             # O(1) M(1)
