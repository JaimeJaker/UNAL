"""
Author: jangulot
Complejidad memoria: O(1) - Solo se usa una variable para contar y un acumulador de tiempo.
Complejidad tiempo: O(n) - En el peor caso se revisan las n preguntas.
"""

n, k = map(int, input().split())  # O(1) M(1)

timepo = 240 - k  # O(1) M(1)

preguntas = 0  # O(1) M(1)

for i in range(1, n + 1):  # O(n) M(1)
    timepo -= 5 * i  # O(1) M(1)

    if timepo < 0:  # O(1) M(1)
        break  # O(1) M(1)
    else:
        preguntas += 1  # O(1) M(1)

print(preguntas)  # O(1) M(1)
