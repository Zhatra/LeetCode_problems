# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #crea una lista llamada dumy
        dumy = ListNode()
        #la llamamos tail
        tail = dumy
        # mientras list1 y list2 no sean vacias
        while list1 and list2:
            #checamos si el valor en el indice de list1 es menor que es valor en el indice cero de list2
            if list1.val < list2.val:
                #le asignamos a nuestra nueva lista list1 como elemento hasta atras
                tail.next = list1
                #y ahora recorremos al siguiente indice en list
                list1 = list1.next
            #si list1 no es menor que list2 hacemos lo contrario
            else:
                tail.next = list2
                list2= list2.next
            tail = tail.next #actualizamos el tail la siguiente indice para que no pongan siempre en el mismo los elementos de list1 o list2

        #esto es para ver si solo una de las listas tiene elementos si es asi solo le asignamo a nuestra lista la lista que si tiene elemntos
        if list1:
            tail.next = list1

        elif list2:
            tail.next = list2


        #regresamos la lista
        return dumy.next
