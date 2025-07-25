public class Lista_Enlazada<T> {
    public static class Nodo<T> {
        public T dato;
        public Nodo<T> next;

        public Nodo(T dato) {
            this.dato = dato;
            this.next = null;
        }
    }

    private Nodo<T> head;

    public Lista_Enlazada() {
        this.head = null;
    }

    // Método para insertar un nuevo elemento en la lista enlazada
    public void insertar(T dato) {
        Nodo<T> nuevo = new Nodo<>(dato);
        if (head == null) {
            head = nuevo;
        } else {
            nuevo.next = head;
            head = nuevo;
        }
    }

    // Método para buscar un elemento en la lista enlazada por clave
    public T buscar(String clave, java.util.function.Function<T, String> claveExtractor) {
        Nodo<T> actual = head;
        while (actual != null) {
            if (claveExtractor.apply(actual.dato).equals(clave)) {
                return actual.dato; // Elemento encontrado
            }
            actual = actual.next;
        }
        return null; // No encontrado
    }

    // Método para eliminar un elemento en la lista enlazada por clave
    public boolean eliminar(String clave, java.util.function.Function<T, String> claveExtractor) {
        if (head == null) return false;

        if (claveExtractor.apply(head.dato).equals(clave)) {
            head = head.next;
            return true; // Eliminado exitosamente
        }

        Nodo<T> actual = head;
        while (actual.next != null) {
            if (claveExtractor.apply(actual.next.dato).equals(clave)) {
                actual.next = actual.next.next;
                return true; // Eliminado exitosamente
            }
            actual = actual.next;
        }

        return false; // No encontrado
    }

    // Obtener todos los elementos de la lista
    public java.util.LinkedList<T> obtenerTodos() {
        java.util.LinkedList<T> elementos = new java.util.LinkedList<>();
        Nodo<T> actual = head;
        while (actual != null) {
            elementos.add(actual.dato);
            actual = actual.next;
        }
        return elementos;
    }

    // Verificar si la lista está vacía
    public boolean estaVacia() {
        return head == null;
    }
}
