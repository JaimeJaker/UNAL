#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int filas, columnas;
    cin >> filas >> columnas;
    vector<string> laberinto(filas);
    for (int i = 0; i < filas; i++) {
        cin >> laberinto[i];
    }
    string ruta;
    cin >> ruta;

    // 1) Posiciones iniciales
    int pacman_fila = -1, pacman_col = -1;
    int fantasma_fila = -1, fantasma_col = -1;
    for (int f = 0; f < filas; f++) {
        for (int c = 0; c < columnas; c++) {
            if (laberinto[f][c] == 'P') {
                pacman_fila = f;
                pacman_col = c;
            }
            if (laberinto[f][c] == 'G') {
                fantasma_fila = f;
                fantasma_col = c;
            }
        }
    }

    // 2) Simular movimientos de Pacman
    vector<vector<int>> tiempos_llegada(filas, vector<int>(columnas, -1));
    int tiempo = 0;
    tiempos_llegada[pacman_fila][pacman_col] = 0;
    int fila_act = pacman_fila;
    int col_act  = pacman_col;
    unordered_map<char, pair<int,int>> direcciones = {{'U',{-1,0}}, {'D',{1,0}}, {'L',{0,-1}}, {'R',{0,1}}};

    for (char mov : ruta) {
        tiempo++;
        auto [df, dc] = direcciones[mov];
        int nf = fila_act + df;
        int nc = col_act  + dc;
        // Teletransporte filas
        if (nf < 0) nf = filas - 1;
        else if (nf >= filas) nf = 0;
        // Teletransporte columnas
        if (nc < 0) nc = columnas - 1;
        else if (nc >= columnas) nc = 0;
        // Mover si no es pared
        if (laberinto[nf][nc] != '#') {
            fila_act = nf;
            col_act = nc;
        }
        tiempos_llegada[fila_act][col_act] = tiempo;
    }
    int tiempo_max = tiempo;

    // 3) BFS del Fantasma
    vector<vector<bool>> visitado(filas, vector<bool>(columnas, false));
    deque<tuple<int,int,int>> cola;
    cola.emplace_back(fantasma_fila, fantasma_col, 0);
    visitado[fantasma_fila][fantasma_col] = true;
    const vector<pair<int,int>> deltas = {{-1,0},{1,0},{0,-1},{0,1}};

    while (!cola.empty()) {
        auto [f, c, pasos] = cola.front();
        cola.pop_front();
        if (pasos > tiempo_max) break;
        int t_llegada = tiempos_llegada[f][c];
        if (t_llegada != -1 && pasos <= t_llegada) {
            cout << "Yes";
            return 0;
        }
        for (auto [df, dc] : deltas) {
            int nf = f + df;
            int nc = c + dc;
            if (nf >= 0 && nf < filas && nc >= 0 && nc < columnas && !visitado[nf][nc] && laberinto[nf][nc] != '#') {
                visitado[nf][nc] = true;
                cola.emplace_back(nf, nc, pasos + 1);
            }
        }
    }
    cout << "No";
    return 0;
}
