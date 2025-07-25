package Estructura_de_datos.Secuenciales;
public class Colas {
    Listas_Enlazada<Integer> cola = new Listas_Enlazada<Integer>(); // Creamos una lista enlazada vacia de enteros llamada "cola"

    public void push(int num) {// Agregamos un elemento a la cola
            cola.add(num);
        }

    public int pop() {// Eliminamos un elemento de la cola y lo retornamos
        return cola.remove(0);
    }

    public boolean isEmpty() {// Comprobamos si la cola esta vacia
        return cola.isEmpty();
    }

    public int size() { // Retornamos el tamanio de la cola
        return cola.size();
    }

    public int peek() {// Retornamos el elemento mas alto de la cola
        return cola.get(0);
    }

    @Override
    public String toString() {// Imprimimos la cola
        return cola.toString();
    }
}
