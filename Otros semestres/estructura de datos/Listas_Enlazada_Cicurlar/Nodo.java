package Listas_Enlazada_Cicurlar_java;

public class Nodo {
    int dato;
    Nodo Siguiente;

    public Nodo(int d){
        dato = d;
    }

    public int getDato() {
        return dato;
    }

    public Nodo getSiguiente() {
        return Siguiente;
    }
    
    public void setSiguiente(Nodo siguiente) {
        Siguiente = siguiente;
    }
}
