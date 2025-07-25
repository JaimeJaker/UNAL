import sys
from collections import deque

def contar_salas():
    input = sys.stdin.readline
    filas, columnas = map(int, input().split())

    mapa = []
    for _ in range(filas):
        linea = input().rstrip('\n')
        mapa.append(linea)

    visitado = [[False]*columnas for _ in range(filas)]
    desplaz = [(-1,0),(1,0),(0,-1),(0,1)]
    salas = 0

    for i in range(filas):
        for j in range(columnas):
            if mapa[i][j] == '.' and not visitado[i][j]:
                salas += 1
                dq = deque([(i,j)])
                visitado[i][j] = True
                while dq:
                    ci, cj = dq.popleft()
                    for di, dj in desplaz:
                        ni, nj = ci+di, cj+dj
                        if 0 <= ni < filas and 0 <= nj < columnas:
                            if mapa[ni][nj] == '.' and not visitado[ni][nj]:
                                visitado[ni][nj] = True
                                dq.append((ni,nj))

    sys.stdout.write(str(salas))

if __name__ == "__main__":
    contar_salas()
