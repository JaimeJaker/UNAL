package Listas_Enlazada_Cicurlar_java;

public class Lista_Circular {
    Nodo Inicio;
    Nodo Fin;
    int size;

    public Lista_Circular(){
        Inicio = null;
        Fin = null;
        size = 0;
    }

    public void Addlista(int d){
        Nodo nuevNodo = new Nodo(d);
        if (Inicio == null) {
            Inicio = nuevNodo;
            Fin = nuevNodo;
            Fin.Siguiente = Inicio;
        }else{
            Fin.Siguiente = nuevNodo;
            Fin = nuevNodo;
            Fin.Siguiente = Inicio;
        }
        size++;
    }

    public int Size(){
        return size;
    }

    public void MostrarLista(){
        Nodo Temp = Inicio;
        if (Temp != null) {
            do {
                System.out.print(Temp.getDato() + " ");
                Temp = Temp.Siguiente;
            } while(Temp != Inicio);
            System.out.println();
        }
    }
}

