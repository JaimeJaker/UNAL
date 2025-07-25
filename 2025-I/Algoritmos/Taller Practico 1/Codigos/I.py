"""
    author: jangulot
    complejidad tiempo: O(k * 9^m)
    complejidad memoria: O(m + N)
"""

import sys  # O(1) M(1)
from typing import List, Tuple  # O(1) M(1)

N = 9  # O(1) M(1)

class Celda:
    def __init__(self, i: int, j: int, opciones: List[int]):  # O(1) M(1)
        self.i = i  # O(1) M(1)
        self.j = j  # O(1) M(1)
        self.opciones = opciones  # O(1) M(1)

def id_box(i: int, j: int) -> int:  # O(1) M(1)
    return (i // 3) * 3 + j // 3  # O(1) M(1)

def backtrack(tablero: List[List[str]], vacias: List[Celda], 
              fila: List[List[bool]], col: List[List[bool]], 
              box: List[List[bool]]) -> bool:  # O(9^m) M(m)
    if not vacias:  # O(1) M(1)
        return True  # O(1) M(1)
    
    vacias.sort(key=lambda x: len(x.opciones))  # O(m log m) M(1)
    actual = vacias.pop(0)  # O(1) M(1)
    
    for num in actual.opciones:  # O(9) M(1)
        if not fila[actual.i][num] and not col[actual.j][num] and not box[id_box(actual.i, actual.j)][num]:  # O(1) M(1)
            tablero[actual.i][actual.j] = str(num)  # O(1) M(1)
            fila[actual.i][num] = col[actual.j][num] = box[id_box(actual.i, actual.j)][num] = True  # O(1) M(1)
            
            nueva_lista = []  # O(1) M(1)
            valido = True  # O(1) M(1)
            
            for c in vacias:  # O(m) M(1)
                posibles = []  # O(1) M(1)
                for d in range(1, 10):  # O(9) M(1)
                    if not fila[c.i][d] and not col[c.j][d] and not box[id_box(c.i, c.j)][d]:  # O(1) M(1)
                        posibles.append(d)  # O(1) M(1)
                if not posibles:  # O(1) M(1)
                    valido = False  # O(1) M(1)
                    break  # O(1) M(1)
                nueva_lista.append(Celda(c.i, c.j, posibles))  # O(1) M(1)
            
            if valido and backtrack(tablero, nueva_lista, fila, col, box):  # O(9^m) M(m)
                return True  # O(1) M(1)
            
            fila[actual.i][num] = col[actual.j][num] = box[id_box(actual.i, actual.j)][num] = False  # O(1) M(1)
            tablero[actual.i][actual.j] = '.'  # O(1) M(1)
    
    vacias.insert(0, actual)  # O(m) M(1)
    return False  # O(1) M(1)

def resolver(tablero: List[List[str]]) -> None:  # O(9^m) M(m + N)
    fila = [[False] * 10 for _ in range(N)]  # O(N) M(N)
    col = [[False] * 10 for _ in range(N)]  # O(N) M(N)
    box = [[False] * 10 for _ in range(N)]  # O(N) M(N)
    
    for i in range(N):  # O(N^2) M(1)
        for j in range(N):  # O(N) M(1)
            if tablero[i][j] != '.':  # O(1) M(1)
                num = int(tablero[i][j])  # O(1) M(1)
                fila[i][num] = col[j][num] = box[id_box(i, j)][num] = True  # O(1) M(1)
    
    vacias = []  # O(1) M(1)
    for i in range(N):  # O(N^2) M(1)
        for j in range(N):  # O(N) M(1)
            if tablero[i][j] == '.':  # O(1) M(1)
                posibles = []  # O(1) M(1)
                for num in range(1, 10):  # O(9) M(1)
                    if not fila[i][num] and not col[j][num] and not box[id_box(i, j)][num]:  # O(1) M(1)
                        posibles.append(num)  # O(1) M(1)
                vacias.append(Celda(i, j, posibles))  # O(1) M(1)
    
    backtrack(tablero, vacias, fila, col, box)  # O(9^m) M(m)

def main():  # O(T * 9^m) M(m + N)
    T = int(input().strip())  # O(1) M(1)
    
    for caso in range(1, T + 1):  # O(T) M(1)
        try:
            input()  # O(1) M(1)
        except:
            pass  # O(1) M(1)
        
        tablero = []  # O(1) M(1)
        for i in range(N):  # O(N) M(1)
            linea = input().strip()  # O(N) M(1)
            tablero.append(list(linea))  # O(N) M(N)
        
        resolver(tablero)  # O(9^m) M(m + N)
        
        print(f"Case {caso}:")  # O(1) M(1)
        for i in range(N):  # O(N) M(1)
            print(''.join(tablero[i]))  # O(N) M(1)

if __name__ == "__main__":  # O(1) M(1)
    main()  # O(T * 9^m) M(m + N)
