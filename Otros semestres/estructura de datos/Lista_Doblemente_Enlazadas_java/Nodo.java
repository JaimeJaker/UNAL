package Lista_Doblemente_Enlazadas_java;

public class Nodo {
    int dato;
    Nodo Siguiente;
    Nodo Anterior;


    public Nodo(int dato) {
        this.dato = dato;
        Siguiente = null;
        Anterior = null;
    }
    

    public Nodo getAnterior() {
        return Anterior;
    }

    public void setAnterior(Nodo anterior) {
        Anterior = anterior;
    }
    
    public Nodo getSiguiente() {
        return Siguiente;
    }
    public void setSiguiente(Nodo siguiente) {
        Siguiente = siguiente;
    }

    public int getDato() {
        return dato;
    }
    
}
