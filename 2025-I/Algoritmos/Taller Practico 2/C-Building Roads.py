import sys
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    padre = list(range(n+1))
    rango = [0]*(n+1)

    def find(u):
        while padre[u] != u:
            padre[u] = padre[padre[u]]
            u = padre[u]
        return u

    def union(u, v):
        ru, rv = find(u), find(v)
        if ru == rv:
            return
        if rango[ru] < rango[rv]:
            padre[ru] = rv
        elif rango[rv] < rango[ru]:
            padre[rv] = ru
        else:
            padre[rv] = ru
            rango[ru] += 1

    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)

    representantes = []
    for i in range(1, n+1):
        if find(i) == i:
            representantes.append(i)

    c = len(representantes)
    sys.stdout.write(str(c-1) + "\n")
    for i in range(c-1):
        u = representantes[i]
        v = representantes[i+1]
        sys.stdout.write(f"{u} {v}\n")

if __name__ == "__main__":
    main()
