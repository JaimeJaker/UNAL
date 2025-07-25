package Lista_Doblemente_Enlazada_Circular_java;

public class Main {
    public static void main(String[] args) {
        
        Doble_lista_Circular ll1 = new Doble_lista_Circular();

        for (int i = 2; i <10; i++){
            ll1.AddLista(i);
        }

        ll1.MostrarLista();
        
    }

}
