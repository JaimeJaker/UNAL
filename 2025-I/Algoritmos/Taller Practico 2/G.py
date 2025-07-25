import sys
import bisect

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))

    # tails[i] será el menor valor final posible de una subsecuencia creciente de longitud i+1
    tails = []

    for x in arr:
        # Encuentra posición para x en tails (primer elemento >= x)
        pos = bisect.bisect_left(tails, x)
        if pos == len(tails):
            # x es mayor que todos, extiende la subsecuencia más larga
            tails.append(x)
        else:
            # Reemplaza para mantener valores finales lo más pequeños posible
            tails[pos] = x

    # La longitud de tails es la respuesta
    print(len(tails))

if __name__ == "__main__":
    main()
