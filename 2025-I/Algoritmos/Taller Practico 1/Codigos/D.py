"""
author: jangulot
complejidad tiempo: O(q * m)   # donde m puede ser el número de notificaciones por app en el peor caso
complejidad memoria: O(n + q)
"""

n, q = map(int, input().split())  # O(1) M(1)
notificaciones = []               # O(1) M(q)
por_app = [[] for _ in range(n + 1)]  # O(n) M(n)
leidas = [0] * (n + 1)            # O(n) M(n)
sin_leer = 0                      # O(1) M(1)
respuestas = []                  # O(1) M(q)
indice = 0                        # O(1) M(1)
leidas_global = 0                # O(1) M(1)

for _ in range(q):               # O(q * m) M(1)
    entrada = input().split()    # O(1) M(1)
    tipo = int(entrada[0])       # O(1) M(1)

    if tipo == 1:
        app = int(entrada[1])    # O(1) M(1)
        notificaciones.append(app)  # O(1) amortizado M(1)
        por_app[app].append(len(notificaciones) - 1)  # O(1) M(1)
        sin_leer += 1            # O(1) M(1)

    elif tipo == 2:
        app = int(entrada[1])    # O(1) M(1)
        # O(m) donde m = len(por_app[app]) - leidas[app]
        for i in range(leidas[app], len(por_app[app])):  # O(m) M(1)
            indice_noti = por_app[app][i]  # O(1) M(1)
            if notificaciones[indice_noti] != -1:  # O(1) M(1)
                notificaciones[indice_noti] = -1   # O(1) M(1)
                sin_leer -= 1                      # O(1) M(1)
        leidas[app] = len(por_app[app])  # O(1) M(1)

    else:
        t = int(entrada[1])      # O(1) M(1)
        while leidas_global < t:  # O(t) M(1)
            if notificaciones[leidas_global] != -1:  # O(1) M(1)
                sin_leer -= 1                        # O(1) M(1)
                notificaciones[leidas_global] = -1   # O(1) M(1)
            leidas_global += 1                      # O(1) M(1)

    respuestas.append(str(sin_leer))  # O(1) M(1)

print('\n'.join(respuestas))  # O(q) M(q)
