import unittest
from typing import List
from typing import Optional
#Basicamente lo que hace este algoritmo es que creamos primero dos punteros val, head a los cuales le asignamos None y head, para despues empezar con un while en el cual ponemos la condicion mientras head sea true, empezamos el algoritmo, primero guardamos en la variable nxth la cabeza siguiente  de head en ese momento, despues asignamos la referencia de la head.next ese momento a val el cual es el elemento anterior a head el cual es None por que antes de la cabeza no hay nada, por lo cual la referencia anteriro de head.next al siguiente elemento quedara vacia por el momento, posterior mente asignamos val a la head del while y posterior mente asignamos a la cabeza en ese momento del while a la siguiente , por lo cual abremos recorrido el val y la cabeza y hemos cambio las referencia hacia el sentido contrario y haremos esto nuevamente hasta que el head no sea true por lo cual regresaremos val que sera la cabeza de la nueva listaNodo invertida
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val,head=None,head

        while head:
            nxth = head.next
            head.next = val
            val = head
            head = nxth
        return val

class TestReverseList(unittest.TestCase):
    def test_reverse_list(self):
        self.assertEqual(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))).next.next.next.next.val, 1)
        self.assertEqual(Solution().reverseList(ListNode(1, ListNode(2))).next.val, 1)
        self.assertEqual(Solution().reverseList(ListNode(2, ListNode(1, ListNode(3, ListNode(4, ListNode(5)))))).next.next.next.next.val, 2)

if __name__ == '__main__':
    unittest.main()
