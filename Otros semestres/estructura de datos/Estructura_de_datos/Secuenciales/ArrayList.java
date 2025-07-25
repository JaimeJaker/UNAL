package Estructura_de_datos.Secuenciales;

public class ArrayList<T> implements List<T> {
    int size;
    T[] elements;

    @SuppressWarnings("unchecked")
    public ArrayList() {
        size = 0;
        elements = (T[]) new Object[10];
    }

    @Override
    public boolean isEmpty() {//comprueba si la lista esta vacia
        return size == 0;
    }

    @Override
    public int size() {// dice el tamaño de la lista
        return size;
    }

    private void resize(int newSize) {//redimensiona la lista cuando se agregan mas elementos del que tiene capacidad actualmente
        @SuppressWarnings("unchecked")
        T[] newElements = (T[]) new Object[newSize];
        System.arraycopy(elements, 0, newElements, 0, size);
        elements = newElements;
    }

    @Override
    public T get(int index) {//devuelve el elemento en la posicion dada por el indice
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException();
        }
        return elements[index];
    }

    @Override
    public int indexOf(T TheElement) {//devuelve el indice del elemento dado por parametro o -1 si no lo encuentra
        for (int i = 0; i < size; i++) {
            if (TheElement.equals(elements[i])) {
                return i;
            }
        }
        return -1;
    }

    @Override
    public T remove(int index) {//elimina el elemento en la posicion dada por el indice y lo devuelve
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException();
        }
        T removedElement = elements[index];
        for (int i = index; i < size - 1; i++) {
            elements[i] = elements[i + 1];
        }
        size--;
        return removedElement;
    }

    @Override
    public void add(int index, T TheElement) {//añade el elemento en la posicion dada por el indice
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException();
        }
        if (size == elements.length) {
            resize(size * 2);
        }
        for (int i = size - 1; i >= index; i--) {
            elements[i + 1] = elements[i];
        }
        elements[index] = TheElement;
        size++;
    }
    @Override
    public String toString() {//devuelve una cadena con los elementos de la lista separados por comas
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < size; i++) {
            sb.append(elements[i]);
            if (i < size - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();
    }

}