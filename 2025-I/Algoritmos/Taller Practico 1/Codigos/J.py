"""
    author: jangulot
    complejidad tiempo: O(8!)
    complejidad memoria: O(8)
"""

def resolver_ocho_reinas():  # O(1) M(1)
    tablero = []  # O(1) M(1)
    for i in range(8):  # O(8) M(1)
        fila = input().strip()  # O(8) M(1)
        tablero.append(fila)  # O(1) M(8)

    reinas = [-1] * 8  # O(1) M(8)
    total_soluciones = 0  # O(1) M(1)
    
    def es_posicion_valida(fila, columna):  # O(fila) M(1)
        if tablero[fila][columna] == '*':  # O(1) M(1)
            return False  # O(1) M(1)
        
        for fila_anterior in range(fila):  # O(fila) M(1)
            columna_anterior = reinas[fila_anterior]  # O(1) M(1)
            if columna_anterior == columna:  # O(1) M(1)
                return False  # O(1) M(1)
            if abs(fila - fila_anterior) == abs(columna - columna_anterior):  # O(1) M(1)
                return False  # O(1) M(1)
        return True  # O(1) M(1)

    def backtracking(fila):  # O(8!) M(8)
        nonlocal total_soluciones  # O(1) M(1)
        
        if fila == 8:  # O(1) M(1)
            total_soluciones += 1  # O(1) M(1)
            return  # O(1) M(1)
        
        for columna in range(8):  # O(8) M(1)
            if es_posicion_valida(fila, columna):  # O(fila) M(1)
                reinas[fila] = columna  # O(1) M(1)
                backtracking(fila + 1)  # O(8!) M(8)
                reinas[fila] = -1  # O(1) M(1)
    
    backtracking(0)  # O(8!) M(8)
    
    print(total_soluciones)  # O(1) M(1)

# Ejecutar la solución
resolver_ocho_reinas()  # O(8!) M(8)
