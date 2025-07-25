package Estructura_de_datos.Secuenciales;

public class Listas_Enlazada<T> {

    private Nodo<T> Inicio;
    private int size;       //tamanio de la lista

    public Listas_Enlazada() {
        Inicio = null;
        size = 0;
    }


    public boolean isEmpty() {//comprueba si la lista esta vacia
        return size == 0;
    }


    public int size() {// dice el tamaño de la lista
        return size;
    }


    public T get(int index) {//devuelve el elemento en la posicion dada por el indice
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException();
        }
        Nodo<T> aux = Inicio;
        for (int i = 0; i < index; i++) {
            aux = aux.getSiguiente();
        }
        return aux.getDato();
    }


    public int indexOf(T TheElement) {//devuelve el indice del elemento dado por parametro o -1 si no lo encuentra
        Nodo<T> aux = Inicio;
        for (int i = 0; i < size; i++) {
            if (TheElement.equals(aux.getDato())) {
                return i;
            }
            aux = aux.getSiguiente();
        }
        return -1;
    }


    public T remove(int index) {//elimina el elemento en la posicion dada por el indice y lo devuelve
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException();
        }
        T removedElement = get(index);
        if (index == 0) {
            Inicio = Inicio.getSiguiente();
        } else {
            Nodo<T> aux = Inicio;
            for (int i = 0; i < index - 1; i++) {
                aux = aux.getSiguiente();
            }
            aux.setSiguiente(aux.getSiguiente().getSiguiente());
        }
        size--;
        return removedElement;
    }

    public void add(T TheElement) {// añade el elemento al final de la lista
        Nodo<T> nuevo = new Nodo<>(TheElement);
        if (isEmpty()) {
            Inicio = nuevo;
        } else {
            Nodo<T> aux = Inicio;
            while (aux.getSiguiente() != null) {
                aux = aux.getSiguiente();
            }
            aux.setSiguiente(nuevo);
        }
        size++;
    }


    public void add(int index, T TheElement) {// añade el elemento en la posicion dada por el indice
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException();
        }
        Nodo<T> nuevo = new Nodo<>(TheElement);
        if (index == 0) {
            nuevo.setSiguiente(Inicio);
            Inicio = nuevo;
        } else {
            Nodo<T> aux = Inicio;
            for (int i = 0; i < index - 1; i++) {
                aux = aux.getSiguiente();
            }
            nuevo.setSiguiente(aux.getSiguiente());
            aux.setSiguiente(nuevo);
        }
        size++;
    }


    public String toString() {//devuelve una cadena con los elementos de la lista separados por comas
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        Nodo<T> aux = Inicio;
        for (int i = 0; i < size; i++) {
            sb.append(aux.getDato());
            if (i < size - 1) {
                sb.append(", ");
            }
            aux = aux.getSiguiente();
        }
        sb.append("]");
        return sb.toString();
    }

    public class Nodo<U> {
        U Dato;
        Nodo<U> Siguiente;

        public Nodo(U d) {
            Dato = d;
            Siguiente = null;
        }

        public U getDato() {
            return Dato;
        }

        public Nodo<U> getSiguiente() {
            return Siguiente;
        }

        public void setSiguiente(Nodo<U> siguiente) {
            Siguiente = siguiente;
        }
    }
}
