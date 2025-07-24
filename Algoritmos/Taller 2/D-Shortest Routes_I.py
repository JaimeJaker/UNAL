import sys
import heapq

def rutas_minimas():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    ady = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        ady[a].append((b, c))
    
    INF = 10**30
    distancia = [INF] * (n+1)
    distancia[1] = 0  
    
    
    heap = [(0, 1)]
    
    while heap:
        dist_u, u = heapq.heappop(heap)
        
        if dist_u > distancia[u]:
            continue
        
        for v, coste in ady[u]:
            nueva_dist = dist_u + coste
            if nueva_dist < distancia[v]:
                distancia[v] = nueva_dist
                heapq.heappush(heap, (nueva_dist, v))
    
    
    out = sys.stdout.write
    for i in range(1, n+1):
        out(str(distancia[i]) + ("\n" if i < n else ""))


if __name__ == "__main__":
    rutas_minimas()
