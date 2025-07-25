"""
    author: jangulot
    complejidad tiempo: O(L^2 * log N)
    complejidad memoria: O(L^2)
    donde L es la longitud del nombre más largo involucrado (nombre/apellido),
    y N es la cantidad de posibles LDAPs generados.
"""

import sys  # O(1) M(1)

def generar_ldap(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, i, j):  # O(i + j + len(apellido)) M(1)
    ldap = primer_nombre[:i]  # O(i) M(i)
    if segundo_nombre:  # O(1) M(1)
        ldap += segundo_nombre[0]  # O(1) M(1)
    ldap += primer_apellido  # O(len) M(len)
    ldap += segundo_apellido[:j]  # O(j) M(j)
    return ldap  # O(1) M(1)

def construir_lista_ldaps(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido):  # O(L^2) M(L^2)
    ln = len(primer_nombre)  # O(1) M(1)
    ls = len(segundo_apellido)  # O(1) M(1)
    lista = []  # O(1) M(1)

    # Fase 1
    for i in range(1, ln + 1):  # O(L)
        inicio_j = 1 if i == 1 else 0  # O(1)
        fin_j = min(i, ls)  # O(1)
        for j in range(inicio_j, fin_j + 1):  # O(L)
            lista.append(generar_ldap(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, i, j))  # O(L) M(L)

    # Fase 2
    for j in range(ln + 1, ls + 1):  # O(L)
        lista.append(generar_ldap(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, ln, j))  # O(L) M(L)

    return lista  # O(1) M(L^2)

def consultar_interactivo(ldap):  # O(1) M(1)
    print(ldap)  # O(1) M(1)
    sys.stdout.flush()  # O(1) M(1)
    respuesta = input().strip()  # O(1) M(1)
    return (respuesta == "0")  # O(1) M(1)

def resolver_ldap_con_busqueda_binaria():  # O(L^2 * log N) M(L^2)
    nombre_completo = input().strip()  # O(1) M(1)
    palabras = nombre_completo.split()  # O(1) M(1)

    if len(palabras) == 3:  # O(1) M(1)
        primer_nombre   = palabras[0]  # O(1) M(1)
        segundo_nombre  = ""  # O(1) M(1)
        primer_apellido = palabras[1]  # O(1) M(1)
        segundo_apellido= palabras[2]  # O(1) M(1)
    else:
        primer_nombre   = palabras[0]  # O(1) M(1)
        segundo_nombre  = palabras[1]  # O(1) M(1)
        primer_apellido = palabras[2]  # O(1) M(1)
        segundo_apellido= palabras[3]  # O(1) M(1)

    candidatos = construir_lista_ldaps(primer_nombre, segundo_nombre,
                                       primer_apellido, segundo_apellido)  # O(L^2) M(L^2)

    lo = 0  # O(1) M(1)
    hi = len(candidatos) - 1  # O(1) M(1)

    while lo < hi:  # O(log N)
        mid = (lo + hi) // 2  # O(1) M(1)
        if consultar_interactivo(candidatos[mid]):  # O(1) M(1)
            hi = mid  # O(1) M(1)
        else:
            lo = mid + 1  # O(1) M(1)

    resultado = candidatos[lo]  # O(1) M(1)
    print(f"! {resultado}")  # O(1) M(1)
    sys.stdout.flush()  # O(1) M(1)

if __name__ == "__main__":  # O(1) M(1)
    resolver_ldap_con_busqueda_binaria()  # O(L^2 * log N) M(L^2)
