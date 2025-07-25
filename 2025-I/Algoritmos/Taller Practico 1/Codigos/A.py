""" 
Author: ldap
Complejidad memoria: O(n) – Se utiliza una lista de tamaño 2n para almacenar los enteros leídos.
Complejidad tiempo: O(n log n) – El tiempo está dominado por la ordenación de la lista.
"""

import sys
input = sys.stdin.readline  # O(1) M(1)

t = int(input())  # O(1) M(1)
for _ in range(t):  # O(t) M(1)
    n = int(input())  # O(1) M(1)
    a = list(map(int, input().split()))  # O(n) M(n) – Se leen 2n números, pero se usa O(n) por el rango principal de n
    
    a.sort()  # O(n log n) M(1) – Ordenar la lista de 2n elementos
    
    # sumamos los elementos en índices 0, 2, 4, ..., 2n−2
    ans = sum(a[i] for i in range(0, 2 * n, 2))  # O(n) M(1) – Se recorre la mitad de la lista para sumar
    
    print(ans)  # O(1) M(1)
