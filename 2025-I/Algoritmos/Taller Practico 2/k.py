import sys
from collections import deque

def resolver():
    entrada = sys.stdin.readline
    # Lectura de dimensiones
    filas, columnas = map(int, entrada().split())
    # Lectura del laberinto
    laberinto = [entrada().rstrip() for _ in range(filas)]
    # Ruta de Pacman
    ruta = entrada().rstrip()

    # 1) Encontrar posiciones iniciales de Pacman y Fantasma
    for f in range(filas):
        fila = laberinto[f]
        if 'P' in fila:
            pacman_fila, pacman_col = f, fila.index('P')
        if 'G' in fila:
            fantasma_fila, fantasma_col = f, fila.index('G')

    # 2) Simular movimientos de Pacman y guardar el último tiempo en cada celda
    tiempos_llegada = {(pacman_fila, pacman_col): 0}
    tiempo = 0
    # Deltas de movimiento
    direcciones = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    fila_act, col_act = pacman_fila, pacman_col
    for mov in ruta:
        tiempo += 1
        df, dc = direcciones[mov]
        nf, nc = fila_act + df, col_act + dc
        # Teletransporte en filas
        if nf < 0:
            nf = filas - 1
        elif nf >= filas:
            nf = 0
        # Teletransporte en columnas
        if nc < 0:
            nc = columnas - 1
        elif nc >= columnas:
            nc = 0
        # Si no hay pared, mover Pacman
        if laberinto[nf][nc] != '#':
            fila_act, col_act = nf, nc
        # Registrar último tiempo en la celda
        tiempos_llegada[(fila_act, col_act)] = tiempo
    tiempo_max = tiempo

    # 3) BFS del Fantasma con poda al tiempo máximo
    visitado = [[False] * columnas for _ in range(filas)]
    cola = deque([(fantasma_fila, fantasma_col, 0)])
    visitado[fantasma_fila][fantasma_col] = True
    ap = cola.append
    pop = cola.popleft
    get_t = tiempos_llegada.get

    while cola:
        fg, cg, pasos = pop()
        # Si superamos el tiempo máximo, terminar
        if pasos > tiempo_max:
            break
        # Verificar captura
        t_llegada = get_t((fg, cg))
        if t_llegada is not None and pasos <= t_llegada:
            sys.stdout.write("Yes")
            return
        # Expandir vecinos
        for df, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nf, nc = fg + df, cg + dc
            if 0 <= nf < filas and 0 <= nc < columnas and not visitado[nf][nc] and laberinto[nf][nc] != '#':
                visitado[nf][nc] = True
                ap((nf, nc, pasos + 1))
    # Si no atrapó a Pacman
    sys.stdout.write("No")

if __name__ == '__main__':
    resolver()
