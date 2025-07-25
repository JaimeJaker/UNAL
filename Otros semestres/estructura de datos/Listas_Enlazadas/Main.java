package Listas_Enlazadas_java;

public class Main {
    public static void main(String[] args) {

       Lista l1 = new Lista();
       l1.AddFinalLista(4);

       l1.MostrarLista();
       System.out.println(" "); 
       System.out.println("el tamaño de la lista es " + l1.size());

       l1.AddFinalLista(5);
       System.out.println(" "); 

       l1.MostrarLista();
       System.out.println(" "); 
       System.out.println("el tamaño de la lista es " + l1.size());

       l1.AddInicioLista(9);
       
       l1.MostrarLista();
       System.out.println(" "); 
       System.out.println("el tamaño de la lista es " + l1.size());


    }
}
