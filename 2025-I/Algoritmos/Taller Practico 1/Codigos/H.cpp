/* 
    author: jangulot
    complejidad tiempo: O(t * n * log n)
    complejidad memoria: O(n)
*/

#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005;
bool es_primo[MAXN];         // O(n) M(n)
int primos_acum[MAXN];       // O(n) M(n)

// Criba de Eratóstenes modificada para contar primos hasta n
void criba(int n) { // O(n log log n) M(n)
    fill(es_primo, es_primo + n + 1, true); // O(n) M(1)
    es_primo[0] = es_primo[1] = false;

    for (int i = 2; i * i <= n; ++i) { // O(n log log n) M(1)
        if (es_primo[i]) {
            for (int j = i * i; j <= n; j += i) {
                es_primo[j] = false;
            }
        }
    }

    primos_acum[0] = primos_acum[1] = 0;
    for (int i = 2; i <= n; ++i) { // O(n) M(1)
        primos_acum[i] = primos_acum[i - 1] + (es_primo[i] ? 1 : 0);
    }
}

// Cuenta los rangos [i, j] con al menos k primos en el rango
long long contar_rangos(int n, int k) { // O(n log n) M(1)
    long long total = 0;

    for (int izq = 2; izq <= n; ++izq) { // O(n) M(1)
        int inicio = izq, fin = n, primer_valido = -1;

        while (inicio <= fin) { // O(log n) M(1)
            int medio = (inicio + fin) / 2;
            int cantidad_primos = primos_acum[medio] - primos_acum[izq - 1]; // O(1) M(1)

            if (cantidad_primos >= k) {
                primer_valido = medio;
                fin = medio - 1;
            } else {
                inicio = medio + 1;
            }
        }

        if (primer_valido != -1) {
            total += n - primer_valido + 1; // O(1) M(1)
        }
    }

    return total;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    int max_n = 0;
    vector<pair<int, int>> casos(t); // O(t) M(t)

    for (int i = 0; i < t; ++i) { // O(t) M(1)
        cin >> casos[i].first >> casos[i].second;
        max_n = max(max_n, casos[i].first);
    }

    criba(max_n); // O(n log log n) M(n)

    for (auto [n, k] : casos) { // O(t * n log n) M(1)
        cout << contar_rangos(n, k) << '\n';
    }

    return 0;
}
