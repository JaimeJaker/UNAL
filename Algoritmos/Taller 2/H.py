def distancia_edicion(cadena1: str, cadena2: str) -> int:
    
    largo1 = len(cadena1)
    largo2 = len(cadena2)

   
    dp = [[0] * (largo2 + 1) for _ in range(largo1 + 1)]

    
    for i in range(largo1 + 1):
        dp[i][0] = i  
    for j in range(largo2 + 1):
        dp[0][j] = j  

    for i in range(1, largo1 + 1):
        for j in range(1, largo2 + 1):
            if cadena1[i - 1] == cadena2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                costo_eliminar   = dp[i - 1][j]
                costo_insertar   = dp[i][j - 1]
                costo_reemplazar = dp[i - 1][j - 1]
                dp[i][j] = 1 + min(costo_eliminar,
                                   costo_insertar,
                                   costo_reemplazar)

    return dp[largo1][largo2]


if __name__ == "__main__":
    cadena1 = input().strip()
    cadena2 = input().strip()
    print(distancia_edicion(cadena1, cadena2))
