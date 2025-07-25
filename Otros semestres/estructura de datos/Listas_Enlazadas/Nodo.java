package Listas_Enlazadas_java;

public class Nodo {
    private int dato;
    Nodo Siguiente;

    public Nodo(int d){
        dato = d;
    }

    public Nodo(int d, Nodo n){
        dato = d;
        Siguiente = n;
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