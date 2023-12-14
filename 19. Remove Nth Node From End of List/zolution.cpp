
 // Definition for singly-linked list.
  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
 




// Definición de la clase Solution y la función removeNthFromEnd
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // Verificar si la lista está vacía
        if (head == nullptr) return nullptr;

        // Contador para el tamaño total de la lista
        int size = 0;
        ListNode* current = head;

        // Contar el número total de nodos en la lista
        while (current != nullptr) {
            size++;
            current = current->next;
        }

        // Si n es igual al tamaño de la lista, eliminar el primer nodo
        // y devolver el nuevo inicio de la lista
        if (n == size) return head->next;

        // Reiniciar current al inicio de la lista
        current = head;

        // Encontrar el nodo justo antes del nodo a eliminar
        for (int i = 1; i < size - n; i++) {
            current = current->next;
        }

        // Cambiar el enlace del nodo actual para saltarse el nodo a eliminar
        // Esto efectivamente elimina el nodo deseado de la lista
        current->next = current->next->next;

        // Devolver el inicio actualizado de la lista
        return head;
    }
};