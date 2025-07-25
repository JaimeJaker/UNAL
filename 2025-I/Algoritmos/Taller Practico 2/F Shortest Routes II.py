import sys

def principal():
    input = sys.stdin.readline
    
    num_ciudades, num_carreteras, num_consultas = map(int, input().split())
    
    INFINITO = float('inf')
    
    distancias = [[INFINITO] * (num_ciudades + 1) for _ in range(num_ciudades + 1)]
    for i in range(1, num_ciudades + 1):
        distancias[i][i] = 0
    
    for _ in range(num_carreteras):
        a, b, c = map(int, input().split())
        if c < distancias[a][b]:
            distancias[a][b] = c
            distancias[b][a] = c
            
    # Floyd-Warshall con una micro-optimización
    for k in range(1, num_ciudades + 1):
        for i in range(1, num_ciudades + 1):
            # Si no hay camino de i a k, no podemos mejorar ninguna ruta pasando por k desde i.
            # Esta línea es la optimización.
            if distancias[i][k] == INFINITO:
                continue
            for j in range(1, num_ciudades + 1):
                distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])
    
    for _ in range(num_consultas):
        a, b = map(int, input().split())
        resultado = distancias[a][b]
        
        if resultado == INFINITO:
            print(-1)
        else:
            print(resultado)

if __name__ == "__main__":
    principal()