MODULO = 10**9 + 7

def contar_caminos(cuadricula):
    n = len(cuadricula)
    dp = [[0] * n for _ in range(n)]

    if cuadricula[0][0] == '.':
        dp[0][0] = 1

    for fila in range(n):
        for columna in range(n):
            if cuadricula[fila][columna] == '*':
                dp[fila][columna] = 0  
            else:
                if fila > 0:
                    dp[fila][columna] += dp[fila-1][columna]
                if columna > 0:
                    dp[fila][columna] += dp[fila][columna-1]
                dp[fila][columna] %= MODULO

    return dp[n-1][n-1]

if __name__ == "__main__":
    n = int(input())
    cuadricula = [input().strip() for _ in range(n)]
    print(contar_caminos(cuadricula))
