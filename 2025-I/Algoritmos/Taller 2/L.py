import sys
from collections import deque

MOD = 10**9 + 7

def main():
    datos = sys.stdin.read().split()
    it = iter(datos)
    num_nodos = int(next(it))
    num_tipos = int(next(it))
    grafo = [[] for _ in range(num_nodos+1)]
    
    for _ in range(num_nodos-1):
        u = int(next(it))
        v = int(next(it))
        grafo[u].append(v)
        grafo[v].append(u)
        
    tipo_maximo_seguridad = int(next(it))
    max_cantidad_k = int(next(it))
    
    padre = [0] * (num_nodos+1)
    hijos = [[] for _ in range(num_nodos+1)]
    visitado = [False] * (num_nodos+1)
    pila = [1]
    visitado[1] = True
    orden = []
    
    while pila:
        nodo_actual = pila.pop()
        orden.append(nodo_actual)
        for vecino in grafo[nodo_actual]:
            if not visitado[vecino]:
                visitado[vecino] = True
                padre[vecino] = nodo_actual
                hijos[nodo_actual].append(vecino)
                pila.append(vecino)
                
    orden.reverse()
    
    dp = [[[0] * (max_cantidad_k+1) for _ in range(3)] for __ in range(num_nodos+1)]
    
    for nodo_actual in orden:
        estado_actual = [[0] * (max_cantidad_k+1) for _ in range(3)]
        estado_actual[0][1] = 1
        estado_actual[1][0] = (tipo_maximo_seguridad - 1) % MOD
        estado_actual[2][0] = (num_tipos - tipo_maximo_seguridad) % MOD
        
        for hijo in hijos[nodo_actual]:
            total_estado0 = [0] * (max_cantidad_k+1)
            total_estado1 = [0] * (max_cantidad_k+1)
            total_estado2 = [0] * (max_cantidad_k+1)
            
            for contador_k in range(max_cantidad_k+1):
                total_estado0[contador_k] = dp[hijo][1][contador_k]
                total_estado1[contador_k] = (dp[hijo][0][contador_k] + dp[hijo][1][contador_k] + dp[hijo][2][contador_k]) % MOD
                total_estado2[contador_k] = (dp[hijo][1][contador_k] + dp[hijo][2][contador_k]) % MOD
                
            nuevo_estado = [[0] * (max_cantidad_k+1) for _ in range(3)]
            
            for estado in range(3):
                if estado == 0:
                    total_hijo = total_estado0
                elif estado == 1:
                    total_hijo = total_estado1
                else:
                    total_hijo = total_estado2
                    
                for contador_k_padre in range(max_cantidad_k+1):
                    if estado_actual[estado][contador_k_padre] == 0:
                        continue
                    for contador_k_hijo in range(0, max_cantidad_k+1 - contador_k_padre):
                        if total_hijo[contador_k_hijo] == 0:
                            continue
                        nuevo_contador = contador_k_padre + contador_k_hijo
                        if nuevo_contador <= max_cantidad_k:
                            nuevo_estado[estado][nuevo_contador] = (
                                nuevo_estado[estado][nuevo_contador] + 
                                estado_actual[estado][contador_k_padre] * total_hijo[contador_k_hijo]
                            ) % MOD
            estado_actual = nuevo_estado
            
        dp[nodo_actual] = estado_actual
        
    total_maneras = 0
    for estado in range(3):
        for contador_k in range(max_cantidad_k+1):
            total_maneras = (total_maneras + dp[1][estado][contador_k]) % MOD
            
    print(total_maneras)

if __name__ == '__main__':
    main()