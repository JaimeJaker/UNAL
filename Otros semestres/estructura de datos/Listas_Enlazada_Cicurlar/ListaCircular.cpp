#include<iostream>
using namespace std;

template <typename T>
class Nodo{

  private:
    T Dato;
    Nodo* Enlace;

  public:

    Nodo(T dato){
      Dato = dato;
      Enlace = nullptr;
    }
    T getDato(){
      return Dato;
    }
    Nodo* getEnlace(){
      return Enlace;
    }
    void setEnlace(Nodo* enlace){
      Enlace = enlace;
    }
};

template <typename U>
class ListaCircular{
private:
    Nodo<U>* Inicio;
    Nodo<U>* Final;

public:
    ListaCircular(){
        Inicio = nullptr;
        Final = nullptr;
    }

    void insertarFinal(U dato){
        Nodo<U>* nuevo = new Nodo<U>(dato);
        if (Inicio == nullptr){
            Inicio = nuevo;
            Final = nuevo;
            Final->setEnlace(Inicio);
        } else {
            Final->setEnlace(nuevo);
            Final = nuevo;
            Final->setEnlace(Inicio);
        }
    }

    void mostrarLista(){
        if (Inicio == nullptr) {
            cout << "La lista está vacía" << endl;
            return;
        }

        Nodo<U>* aux = Inicio;
        do {
            cout << aux->getDato() << endl;
            aux = aux->getEnlace();
        } while (aux != Inicio);
    }
};

int main(){
    ListaCircular<int>* lista = new ListaCircular<int>();
    lista->insertarFinal(5);
    lista->insertarFinal(6);
    lista->insertarFinal(7);
    lista->insertarFinal(8);
    lista->mostrarLista();

    return 0;
}