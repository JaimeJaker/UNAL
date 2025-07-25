def libreria_mochila():
    
    n, presupuesto_maximo = map(int, input().split())
    precios = list(map(int, input().split()))
    paginas = list(map(int, input().split()))
    
    
    dp = [[0 for _ in range(presupuesto_maximo + 1)] for _ in range(n + 1)]
    
    for libro_actual in range(1, n + 1):
        precio_libro = precios[libro_actual - 1]
        paginas_libro = paginas[libro_actual - 1]
        
        for presupuesto_disponible in range(presupuesto_maximo + 1):
            dp[libro_actual][presupuesto_disponible] = dp[libro_actual - 1][presupuesto_disponible]
            
            if precio_libro <= presupuesto_disponible:
                paginas_con_libro = dp[libro_actual - 1][presupuesto_disponible - precio_libro] + paginas_libro
                dp[libro_actual][presupuesto_disponible] = max(
                    dp[libro_actual][presupuesto_disponible],
                    paginas_con_libro
                )
    
    print(dp[n][presupuesto_maximo])

def solucion_optimizada():
    
    n, presupuesto_maximo = map(int, input().split())
    precios = list(map(int, input().split()))
    paginas = list(map(int, input().split()))
    
    dp = [0] * (presupuesto_maximo + 1)
    
    for i in range(n):
        precio_libro = precios[i]
        paginas_libro = paginas[i]
        
        for presupuesto in range(presupuesto_maximo, precio_libro - 1, -1):
            dp[presupuesto] = max(dp[presupuesto], dp[presupuesto - precio_libro] + paginas_libro)
    
    print(dp[presupuesto_maximo])

def probar_ejemplo():

    n, presupuesto_maximo = 4, 10
    precios = [4, 8, 5, 3]
    paginas = [5, 12, 8, 1]
    
    dp = [0] * (presupuesto_maximo + 1)
    
    for i in range(n):
        precio_libro = precios[i]
        paginas_libro = paginas[i]
        
        for presupuesto in range(presupuesto_maximo, precio_libro - 1, -1):
            dp[presupuesto] = max(dp[presupuesto], dp[presupuesto - precio_libro] + paginas_libro)
    
    print(f"Máximo número de páginas: {dp[presupuesto_maximo]}")
    
    presupuesto_usado = presupuesto_maximo
    libros_seleccionados = []
    
    dp_completa = [[0 for _ in range(presupuesto_maximo + 1)] for _ in range(n + 1)]
    
    for libro in range(1, n + 1):
        precio_libro = precios[libro - 1]
        paginas_libro = paginas[libro - 1]
        
        for presup in range(presupuesto_maximo + 1):
            dp_completa[libro][presup] = dp_completa[libro - 1][presup]
            
            if precio_libro <= presup:
                dp_completa[libro][presup] = max(
                    dp_completa[libro][presup],
                    dp_completa[libro - 1][presup - precio_libro] + paginas_libro
                )
    
    presup = presupuesto_maximo
    for libro in range(n, 0, -1):
        if dp_completa[libro][presup] != dp_completa[libro - 1][presup]:
            libros_seleccionados.append(libro)
            presup -= precios[libro - 1]
    
    libros_seleccionados.reverse()
    print(f"Libros seleccionados: {libros_seleccionados}")
    
    precio_total = sum(precios[i-1] for i in libros_seleccionados)
    paginas_total = sum(paginas[i-1] for i in libros_seleccionados)
    print(f"Precio total: {precio_total}")
    print(f"Páginas total: {paginas_total}")

if __name__ == "__main__":
    solucion_optimizada()