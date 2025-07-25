import java.util.Iterator;
import java.util.NoSuchElementException;

class Node {
    int data;
    Node prev;
    Node next;

    public Node(int data) {
        this.data = data;
        this.prev = null;
        this.next = null;
    }
}

class DoublyLinkedList {
    private Node head;
    private Node tail;

    public DoublyLinkedList() {
        this.head = null;
        this.tail = null;
    }

    // Método para agregar un nodo al final de la lista
    public void append(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
    }

    // Método para agregar un nodo al principio de la lista
    public void prepend(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            newNode.next = head;
            head.prev = newNode;
            head = newNode;
        }
    }

    // Método para imprimir la lista
    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " <-> ");
            current = current.next;
        }
        System.out.println("null");
    }

    // Eliminar un nodo por valor
    public void delete(int data) {
        Node current = head;
        while (current != null) {
            if (current.data == data) {
                if (current == head) {
                    head = current.next;
                    if (head != null) {
                        head.prev = null;
                    }
                } else if (current == tail) {
                    tail = current.prev;
                    tail.next = null;
                } else {
                    current.prev.next = current.next;
                    current.next.prev = current.prev;
                }
                return;
            }
            current = current.next;
        }
    }

    // Obtener el tamaño de la lista
    public int size() {
        int count = 0;
        Node current = head;
        while (current != null) {
            count++;
            current = current.next;
        }
        return count;
    }

    // Obtener el valor en una posición específica
    public int get(int index) {
        if (index < 0 || index >= size()) {
            throw new IndexOutOfBoundsException("Índice fuera de rango");
        }
    
        Node current = head;
        for (int i = 0; i < index; i++) {
            current = current.next;
        }
        return current.data;
    }

    // Invertir la lista
    public void reverse() {
        Node current = head;
        Node temp = null;
        while (current != null) {
            temp = current.prev;
            current.prev = current.next;
            current.next = temp;
            current = current.prev;
        }
        temp = head;
        head = tail;
        tail = temp;
    }

    // Método para obtener un iterador para la lista
public Iterator<Integer> iterator() {
    return new Iterator<Integer>() {
        private Node current = head;

        @Override
        public boolean hasNext() {
            return current != null;
        }

        @Override
        public Integer next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            int data = current.data;
            current = current.next;
            return data;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }
    };
}

// Método para obtener una representación de cadena de la lista
@Override
public String toString() {
    StringBuilder sb = new StringBuilder();
    Node current = head;
    sb.append("DoublyLinkedList: ");
    while (current != null) {
        sb.append(current.data);
        if (current.next != null) {
            sb.append(" <-> ");
        }
        current = current.next;
    }
    return sb.toString();   
}


public static void main(String[] args) {
    DoublyLinkedList myList = new DoublyLinkedList();

    // Agregar elementos al principio y al final de la lista
    myList.append(1);
    myList.append(2);
    myList.prepend(0);

    // Imprimir la lista
    myList.printList(); 

    // Eliminar un elemento
    myList.delete(1);

    // Imprimir la lista después de eliminar
    myList.printList();

    // Obtener el tamaño de la lista
    int size = myList.size();
    System.out.println("Tamaño de la lista: " + size); 

    // Obtener un elemento en una posición específica
    int element = myList.get(1);
    System.out.println("Elemento en la posición 1: " + element);

    // Invertir la lista
    myList.reverse();
    myList.printList();

    // Utilizar un iterador para recorrer la lista
    Iterator<Integer> iterator = myList.iterator();
    while (iterator.hasNext()) {
        int value = iterator.next();
        System.out.print(value + " ");
    }
    System.out.println(); 

    }
}