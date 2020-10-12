class Solution:
    def flatten(self, head):
        res = []
        start = head
        while head:
            if head.child:#если имеем дочерний узел
                if head.next:#если имеем последующий узел
                    res.append(head.next)#то оставшие узлы добавить в массив
                head.next = head.child#псоледующий узел будет равен дочернему
                head.next.prev = head#головной узел
                head.child = None#дочерний узел не имеет поведения

            if head.next is None and len(res) != 0:
                head.next = res.pop()#крайний узел
                head.next.prev = head#головной узел

            head = head.next

        return start



        # node = head
        # while node:
        #
        #     if node.child:
        #
        #         old_next = node.next
        #         node.next = self.flatten(node.child)#если будет дочерний узел у дочернего узла
        #                                              #то след узел будет равен ему
        #         node.next.prev = node
        #         node.child = None
        #
        #         while node.next:
        #             node = node.next
        #
        #         node.next = old_next
        #
        #         if old_next:
        #             old_next.prev = node
        #
        #     node = node.next
        # return head
