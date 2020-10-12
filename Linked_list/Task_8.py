class Solution:
    def oddEvenList(self, head):

        if head or head.next is None:
            return head
        odd = head#нечетный узел равен первому узлу
        even = head.next#четный узел равен следующему
        even_head = even#головной четный узел равен первому четному узлу
        while even and even.next:#пока имеем четное число и четное число +1
            odd.next = even.next#нечетный следующий равен четному следующему
            odd = odd.next#перпемещаем нечетный узел
            even.next = odd.next#четный следующий равен нечетному следующему
            even = even.next#перемещаем четный узел

        odd.next = even_head#после псоледнего нечетного узла начинаются четные узлы
        return head


        # if head is None or head.next is None:
        #     return head
        # odd = head
        # even = head.next
        # even_start = even
        # while even and even.next:
        #     odd.next = even.next
        #     even.next = even.next.next
        #     odd.next.next = even_start
        #     odd = odd.next
        #     even = even.next
        # return head