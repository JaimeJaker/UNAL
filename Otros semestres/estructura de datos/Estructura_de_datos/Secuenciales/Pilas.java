package Estructura_de_datos.Secuenciales;

public class Pilas {
    Listas_Enlazada<Integer> pila = new Listas_Enlazada<Integer>(); // Creamos una lista enlazada vacia

    public void push(int num) {// Agregamos un elemento a la pila
            pila.add(num);
        }

    public int pop() {// Eliminamos un elemento de la pila y lo retornamos
        return pila.remove(pila.size() - 1);
    }

    public boolean isEmpty() {// Comprobamos si la pila esta vacia
        return pila.isEmpty();
    }

    public int size() { // Retornamos el tamanio de la pila
        return pila.size();
    }

    public int peek() {// Retornamos el elemento mas alto de la pila
        return pila.get(pila.size() - 1);
    }

    @Override
    public String toString() {// Imprimimos la pila
        return pila.toString();
    }
}