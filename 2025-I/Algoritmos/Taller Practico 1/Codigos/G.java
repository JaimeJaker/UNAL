/*
    author: jangulot
    complejidad tiempo: O(t * log N + N)
    complejidad memoria: O(N + t)
*/

import java.io.*;
import java.util.*;

public class G {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // O(1) M(1)
        int t = Integer.parseInt(br.readLine());  // O(1) M(1)
        int[] consultas = new int[t];             // O(t) M(t)
        int leidos = 0;                           // O(1) M(1)

        // Leer todas las consultas en el arreglo (soporta múltiples en una sola línea)
        while (leidos < t) {                      // O(t) M(1)
            StringTokenizer st = new StringTokenizer(br.readLine()); // O(1) M(1)
            while (st.hasMoreTokens() && leidos < t) {
                consultas[leidos++] = Integer.parseInt(st.nextToken()); // O(1) M(1)
            }
        }

        int N = 10_000_000;                       // límite superior para búsqueda
        double[] logfact = new double[N + 1];     // O(N) M(N)

        // Precomputar logaritmos de factoriales: logfact[i] = log(i!)
        for (int i = 1; i <= N; i++) {            // O(N) M(1)
            logfact[i] = logfact[i - 1] + Math.log(i); // O(1) M(1)
        }

        StringBuilder sb = new StringBuilder();   // O(1) M(t)

        // Procesar cada consulta
        for (int a : consultas) {                 // O(t * log N) M(1)
            double la = Math.log(a);              // O(1) M(1)
            int lo = 1, hi = N;
            // Búsqueda binaria para encontrar el menor `n` tal que:
            // log(n!) > n * log(a) ⇒ n! > a^n
            while (lo < hi) {                     // O(log N) M(1)
                int mid = lo + (hi - lo) / 2;     // O(1) M(1)
                if (logfact[mid] > mid * la) {    // O(1) M(1)
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }
            sb.append(lo).append('\n');           // O(1) M(1)
        }

        System.out.print(sb);                     // O(t) M(1)
    }
}
