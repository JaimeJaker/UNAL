package Lista_Doblemente_Enlazada_Circular_java;

public class Doble_lista_Circular {
    Nodo Inicio;
    Nodo Fin;

    public Doble_lista_Circular() {
        Inicio = null;
        Fin = null;
    }

    public void AddLista(int d) {
        Nodo nuevo = new Nodo(d);
        if (Inicio == null) {
            Inicio = nuevo;
            Fin = nuevo;
            Fin.Siguiente = Inicio; //Punteros que parecen punteros pero no son punteros XD
            Inicio.Anterior = Fin;
        } else {
            nuevo.Anterior = Fin;
            Fin.Siguiente = nuevo;
            Fin = nuevo;
            Fin.Siguiente = Inicio; 
            Inicio.Anterior = Fin; 
        }
    }
    
    public void MostrarLista() {
        Nodo temporal = Inicio;
        do {
            System.out.print(temporal.getDato() + " ");
            temporal = temporal.Siguiente;
        } while (temporal != Inicio); 
    }

}
