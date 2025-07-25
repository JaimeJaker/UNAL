public class TablaHash {
    private class Entrada {
        String clave;
        Contacto valor;

        public Entrada(String clave, Contacto valor) {
            this.clave = clave;
            this.valor = valor;
        }
    }

    private Lista_Enlazada<Entrada>[] tabla;
    private int capacidad;

    @SuppressWarnings("unchecked")
    public TablaHash(int capacidad) {
        this.capacidad = capacidad;
        tabla = new Lista_Enlazada[capacidad];
        for (int i = 0; i < capacidad; i++) {
            tabla[i] = new Lista_Enlazada<>();
        }
    }

    // Función hash simple
    private int hash(String clave) {
        return Math.abs(clave.hashCode()) % capacidad;
    }

    // Método para insertar un contacto en la tabla hash
    public void insertar(String clave, Contacto valor) {
        int indice = hash(clave);
        Entrada nuevaEntrada = new Entrada(clave, valor);
        tabla[indice].insertar(nuevaEntrada);
    }

    // Método para buscar un contacto por clave
    public Contacto buscar(String clave) {
        int indice = hash(clave);
        Entrada entrada = tabla[indice].buscar(clave, e -> e.clave);
        return entrada != null ? entrada.valor : null;
    }

    // Método para eliminar un contacto por clave
    public boolean eliminar(String clave) {
        int indice = hash(clave);
        return tabla[indice].eliminar(clave, e -> e.clave);
    }

    // Método para obtener todos los contactos
    public java.util.LinkedList<Contacto> obtenerTodos() {
        java.util.LinkedList<Contacto> todosLosContactos = new java.util.LinkedList<>();
        for (Lista_Enlazada<Entrada> lista : tabla) {
            for (Entrada entrada : lista.obtenerTodos()) {
                todosLosContactos.add(entrada.valor);
            }
        }
        return todosLosContactos;
    }

    // Método para verificar si la tabla está vacía
    public boolean estaVacia() {
        for (Lista_Enlazada<Entrada> lista : tabla) {
            if (!lista.estaVacia()) {
                return false;
            }
        }
        return true;
    }
}
