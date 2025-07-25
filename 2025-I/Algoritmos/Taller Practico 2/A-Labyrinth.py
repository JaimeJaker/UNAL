import sys
from collections import deque

def resolver_laberinto():
    input = sys.stdin.readline
    
    # Leer dimensiones
    n, m = map(int, input().split())
    
    # Leer laberinto y localizar A y B (convertidos a índice plano id = i*m + j)
    laberinto = []
    inicio = fin = -1
    for i in range(n):
        fila = input().rstrip()
        laberinto.append(fila)
        if inicio < 0 or fin < 0:
            # solo buscamos mientras no los encontremos
            for j, c in enumerate(fila):
                if c == 'A':
                    inicio = i*m + j
                elif c == 'B':
                    fin    = i*m + j
    
    # Movimientos: L, R, U, D
    # Para índice plano id: 
    #   L => id-1      si j>0
    #   R => id+1      si j<m-1
    #   U => id-m      si i>0
    #   D => id+m      si i<n-1
    dirs = (
        ('L',  0, -1, -1),
        ('R',  0, +1, +1),
        ('U', -1,  0, -m),
        ('D', +1,  0, +m),
    )
    
    total = n*m
    visitado   = [False] * total
    padre_dir  = ['']    * total
    padre_id   = [-1]    * total
    
    dq = deque([inicio])
    visitado[inicio] = True
    
    encontrado = False
    while dq:
        u = dq.popleft()
        if u == fin:
            encontrado = True
            break
        i, j = divmod(u, m)
        for letra, di, dj, delta in dirs:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m:
                v = u + delta
                if not visitado[v] and laberinto[ni][nj] != '#':
                    visitado[v]  = True
                    padre_id[v]  = u
                    padre_dir[v] = letra
                    dq.append(v)
    
    if not encontrado:
        print("NO")
        return
    
    # Reconstruir camino
    camino = []
    cur = fin
    while cur != inicio:
        camino.append(padre_dir[cur])
        cur = padre_id[cur]
    camino.reverse()
    
    # Salida
    print("YES")
    print(len(camino))
    print(''.join(camino))


if __name__ == "__main__":
    resolver_laberinto()
