import sys

def main():
    try:
        primera_linea = input().strip().split()
        n, m = int(primera_linea[0]), int(primera_linea[1])
    except:
        n, m = map(int, input().split())
    
    aristas = []
    for _ in range(m):
        try:
            linea = input().strip().split()
            u, v, w = int(linea[0]), int(linea[1]), int(linea[2])
            aristas.append((u, v, w))
        except:
            u, v, w = map(int, input().split())
            aristas.append((u, v, w))
    
    distancia = [0] * (n+1)
    padre = [-1] * (n+1)
    x = -1
    

    for _ in range(1, n+1):
        x = -1
        for u, v, w in aristas:
            if distancia[u] + w < distancia[v]:
                distancia[v] = distancia[u] + w
                padre[v] = u
                x = v
        if x == -1:
            break
    
    if x == -1:
        print("NO")
        return
    
    for _ in range(n):
        x = padre[x]
    
    
    ciclo = []
    v = x
    while True:
        ciclo.append(v)
        v = padre[v]
        if v == x:
            ciclo.append(v)
            break
    ciclo.reverse()
    
    
    print("YES")
    print(*ciclo)

if __name__ == "__main__":
    main()