#include <iostream>
using namespace std;

template <typename T>
class Nodo{
  public:
    T Dato;
    Nodo* Enlace;

    Nodo(T dato){
      Dato = dato;
      Enlace = NULL;
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
class Lista{
  private:
    Nodo<U>* Inicio;
    Nodo<U>* Final;

  public:
    Lista(){
      Inicio = nullptr;
      Final = nullptr;
    }

    void insertarFinal(U dato){
      Nodo<U>* nuevo = new Nodo<U>(dato);
      if(Inicio == nullptr){
        Inicio = nuevo;
        Final = nuevo;
      }else{
        Final->setEnlace(nuevo);
        Final = nuevo;
      }
    }
    void MostrarLista(){
      Nodo<U>* aux = Inicio;
      while(aux != nullptr){
        cout << aux->getDato() << endl;
        aux = aux->getEnlace();
      }
    }

};

int main(){

  Lista<int>* lista = new Lista<int>();
  lista->insertarFinal(5);
  lista->insertarFinal(6);
  lista->insertarFinal(7);
  lista->insertarFinal(8);

  lista->MostrarLista();

  return 0;
}