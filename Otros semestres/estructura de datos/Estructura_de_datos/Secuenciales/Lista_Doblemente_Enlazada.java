package Estructura_de_datos.Secuenciales;
public class Lista_Doblemente_Enlazada<T> implements List<T> {

    private Nodo cabeza;
    @SuppressWarnings("unused")
    private Nodo cola;
    private int size;

    public Lista_Doblemente_Enlazada() {
        cabeza = null;
        cola = null;
        size = 0;
    }

    @Override
    public boolean isEmpty() {//comprueba si la lista esta vacia
        return size == 0;
    }

    @Override
    public int size() {// dice el tamaño de la lista
        return size;
    }

    @Override
    public T get(int index) {//devuelve el elemento en la posicion dada por el indice(Nodo)
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException();
        }
        Nodo aux = cabeza;
        for (int i = 0; i < index; i++) {
            aux = aux.getSiguiente();
        }
        return (T) aux.getDato();
    }

    @Override
    public int indexOf(T TheElement) {//devuelve el indice del elemento dado por parametro o -1 si no lo encuentra
        Nodo aux = cabeza;
        for (int i = 0; i < size; i++) {
            if (TheElement.equals(aux.getDato())) {
                return i;
            }
            aux = aux.getSiguiente();
        }
        return -1;
    }

    @Override
    public void add(int index, T TheElement) {// añade el elemento en la posicion dada por el indice
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException();
        }
        Nodo nuevo = new Nodo(TheElement);
        if (index == 0) {
            if (isEmpty()) {
                cabeza = nuevo;
                cola = nuevo;
            } else {
                nuevo.setSiguiente(cabeza);
                cabeza.setAnterior(nuevo);
                cabeza = nuevo;
            }
        } else {
            Nodo aux = cabeza;
            for (int i = 0; i < index - 1; i++) {
                aux = aux.getSiguiente();
            }
            nuevo.setSiguiente(aux.getSiguiente());
            nuevo.setAnterior(aux);
            if (aux.getSiguiente() != null) {
                aux.getSiguiente().setAnterior(nuevo);
            }
            aux.setSiguiente(nuevo);
            if (index == size) {
                cola = nuevo;
            }
        }
        size++;
    }
    

    /**
     * @param index
     * @return
     */
    @Override
    public T remove(int index) {//elimina el elemento en la posicion dada por el indice y lo devuelve
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException();
        }
        T removedElement = get(index);
        if (index == 0) {
            cabeza = cabeza.getSiguiente();
            cabeza.setAnterior(null);
        } else {
            Nodo aux = cabeza;
            for (int i = 0; i < index - 1; i++) {
                aux = aux.getSiguiente();
            }
            aux.setSiguiente(aux.getSiguiente().getSiguiente());
            aux.getSiguiente().setAnterior(aux);
        }
        size--;
        return removedElement;
    }

    /**
     * @return
     */
    @Override
    public String toString() {//muestra los elementos de la lista separados por espacios por comas y un espacio
        String result = "";
        Nodo aux = cabeza;
        for (int i = 0; i < size; i++) {
            result += aux.getDato() + " ";
            aux = aux.getSiguiente();
        }
        return result;
    }

    public class Nodo {
        private T dato;
        private Nodo siguiente;
        private Nodo anterior;

        public Nodo(T dato) {
            this.dato = dato;
            this.siguiente = null;
            this.anterior = null;
        }

        public T getDato() {
            return dato;
        }

        public Nodo getAnterior() {
            return anterior;
        }

        public Nodo getSiguiente() {
            return siguiente;
        }
        public void setAnterior(Nodo anterior) {
            this.anterior = anterior;
        }

        public void setSiguiente(Nodo siguiente) {
            this.siguiente = siguiente;
        }
        
    }
}
