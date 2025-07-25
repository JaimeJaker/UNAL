import java.io.*;
import java.util.*;

// Toco hacerlo en Java porque en el juez online era nuy lento con Python
public class K {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int filas = Integer.parseInt(st.nextToken());
        int columnas = Integer.parseInt(st.nextToken());

        // Lectura del laberinto
        char[][] laberinto = new char[filas][columnas];
        for (int i = 0; i < filas; i++) {
            String linea = br.readLine();
            laberinto[i] = linea.toCharArray();
        }
        // Lectura de la ruta
        String ruta = br.readLine();

        // 1) Posiciones iniciales de Pacman y Fantasma
        int pacmanFila = -1, pacmanCol = -1;
        int fantasmaFila = -1, fantasmaCol = -1;
        for (int f = 0; f < filas; f++) {
            for (int c = 0; c < columnas; c++) {
                if (laberinto[f][c] == 'P') {
                    pacmanFila = f;
                    pacmanCol = c;
                } else if (laberinto[f][c] == 'G') {
                    fantasmaFila = f;
                    fantasmaCol = c;
                }
            }
        }

        // 2) Simular movimientos de Pacman y guardar tiempos de llegada
        int[][] tiemposLlegada = new int[filas][columnas];
        for (int[] fila : tiemposLlegada) Arrays.fill(fila, -1);
        int tiempo = 0;
        tiemposLlegada[pacmanFila][pacmanCol] = 0;

        int filaAct = pacmanFila;
        int colAct = pacmanCol;
        Map<Character, int[]> direcciones = new HashMap<>();
        direcciones.put('U', new int[]{-1, 0});
        direcciones.put('D', new int[]{1, 0});
        direcciones.put('L', new int[]{0, -1});
        direcciones.put('R', new int[]{0, 1});

        for (char mov : ruta.toCharArray()) {
            tiempo++;
            int[] d = direcciones.get(mov);
            int nf = filaAct + d[0];
            int nc = colAct + d[1];
            // Teletransporte filas
            if (nf < 0) nf = filas - 1;
            else if (nf >= filas) nf = 0;
            // Teletransporte columnas
            if (nc < 0) nc = columnas - 1;
            else if (nc >= columnas) nc = 0;
            // Mover si no es pared
            if (laberinto[nf][nc] != '#') {
                filaAct = nf;
                colAct = nc;
            }
            tiemposLlegada[filaAct][colAct] = tiempo;
        }
        int tiempoMax = tiempo;

        // 3) BFS del Fantasma con poda al tiempo máximo
        boolean[][] visitado = new boolean[filas][columnas];
        ArrayDeque<int[]> cola = new ArrayDeque<>();
        cola.add(new int[]{fantasmaFila, fantasmaCol, 0});
        visitado[fantasmaFila][fantasmaCol] = true;

        int[][] deltas = {{-1,0},{1,0},{0,-1},{0,1}};

        while (!cola.isEmpty()) {
            int[] actual = cola.poll();
            int f = actual[0], c = actual[1], pasos = actual[2];
            if (pasos > tiempoMax) break;
            int tLlegada = tiemposLlegada[f][c];
            if (tLlegada != -1 && pasos <= tLlegada) {
                System.out.print("Yes");
                return;
            }
            for (int[] delta : deltas) {
                int nf = f + delta[0];
                int nc = c + delta[1];
                if (nf >= 0 && nf < filas && nc >= 0 && nc < columnas && !visitado[nf][nc] && laberinto[nf][nc] != '#') {
                    visitado[nf][nc] = true;
                    cola.add(new int[]{nf, nc, pasos + 1});
                }
            }
        }
        System.out.print("No");
    }
}
