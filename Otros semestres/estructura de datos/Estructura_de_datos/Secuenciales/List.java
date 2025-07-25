package Estructura_de_datos.Secuenciales;

public interface List<T> {
    boolean isEmpty();
    int size();
    T get(int index);
    int indexOf(T TheElement);
    T remove(int index);
    void add(int index, T TheElement);
    String toString();

    //hay 7 metodos

}
