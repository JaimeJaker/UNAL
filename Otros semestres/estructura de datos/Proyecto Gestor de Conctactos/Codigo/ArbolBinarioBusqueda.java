public class ArbolBinarioBusqueda {
    private class Nodo {
        Contacto dato;
        Nodo izquierda, derecha;

        public Nodo(Contacto dato) {
            this.dato = dato;
            this.izquierda = null;
            this.derecha = null;
        }
    }

    private Nodo raiz;

    public ArbolBinarioBusqueda() {
        raiz = null;
    }

    public void insertar(Contacto contacto) {
        raiz = insertarRecursivo(raiz, contacto);
    }

    private Nodo insertarRecursivo(Nodo raiz, Contacto contacto) {
        if (raiz == null) {
            raiz = new Nodo(contacto);
            return raiz;
        }
        if (contacto.nombre.compareTo(raiz.dato.nombre) < 0) {
            raiz.izquierda = insertarRecursivo(raiz.izquierda, contacto);
        } else if (contacto.nombre.compareTo(raiz.dato.nombre) > 0) {
            raiz.derecha = insertarRecursivo(raiz.derecha, contacto);
        }
        return raiz;
    }

    public Contacto buscar(String nombre) {
        return buscarRecursivo(raiz, nombre);
    }

    private Contacto buscarRecursivo(Nodo raiz, String nombre) {
        if (raiz == null || raiz.dato.nombre.equals(nombre)) {
            return raiz != null ? raiz.dato : null;
        }
        if (nombre.compareTo(raiz.dato.nombre) < 0) {
            return buscarRecursivo(raiz.izquierda, nombre);
        }
        return buscarRecursivo(raiz.derecha, nombre);
    }
}
