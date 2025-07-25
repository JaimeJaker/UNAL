package Listas_Enlazadas_java;

public class Lista {
    Nodo Incio;
    Nodo Fin;
    int size;

    public Lista(){
      Incio =  null;
      Fin = null;
      size = 0;
    }

    public void AddFinalLista(int d){
        Nodo nuevo = new Nodo(d);
        if (Incio == null) {
            Incio = nuevo;
            Fin = nuevo;
        }else{
            Fin.setSiguiente(nuevo);
            Fin = nuevo;
        }
        size++;
    }

    public void AddInicioLista(int d){
        Nodo nuevo = new Nodo(d);
        if (Incio == null) {
            Incio = nuevo;
            Fin = nuevo;
        } else {
            nuevo.setSiguiente(Incio);
            Incio = nuevo;
        }
        size++;
    }
    
    public void borrarLista(int d){
        if (Incio != null ){ // 1
            if (Incio == Fin && Incio.getDato() == d) { // 2
                Incio = Fin = null;
            } else if (Incio.getDato() == d) { // 3
                Incio = Incio.Siguiente;
            } else { // 4
                Nodo previo, temporal;
                previo = Incio;
                temporal = Incio.Siguiente;
                while (temporal != null && temporal.getDato() != d) { // 5
                    previo = previo.Siguiente;
                    temporal = temporal.Siguiente;
                }
                if (temporal != null) { // 6
                    previo.Siguiente = temporal.Siguiente;
                    if (temporal == Fin) { // 7
                        Fin = previo;
                    }
                }
            }
        }

        size--;
    }

    public int size() {
        return size;
    }
    

    public void MostrarLista(){
            Nodo Temp = Incio;
            while (Temp != null) {
                System.out.print(Temp.getDato() + " ");
                Temp = Temp.Siguiente;
                
            }
    }

}
