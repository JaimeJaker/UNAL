package Estructura_de_datos.Secuenciales;

public class Main {
    public static void main(String[] args) {

        Pilas pila = new Pilas();
        pila.push(1);
        pila.push(2);
        pila.push(3);
        pila.push(4);

        System.out.println(pila); 

        pila.pop();
        System.out.println(pila); 
        int tope = pila.peek();
        System.out.println(tope); // Imprime: 3
    }
}
