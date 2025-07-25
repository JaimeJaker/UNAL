package Lista_Doblemente_Enlazadas_java;

public class Doble_lista {
    Nodo Inicio;
    Nodo Fin;

    public Doble_lista() {
        Inicio = null;
        Fin = null;
    }
    

    public void Addlista(int d){
        Nodo nuevo = new Nodo(d);
        if (Inicio == null) {
            Fin = nuevo;
            Inicio = nuevo;
        }else{
            nuevo.setAnterior(Fin);
            Fin.setSiguiente(nuevo);
            Fin = nuevo;
        }
    }

    public void MostrarLista(){
        Nodo temporal = Inicio;
        while (temporal != null) {
            System.out.print(temporal.getDato()+ " ");
            temporal = temporal.Siguiente;
        }
    }
}
