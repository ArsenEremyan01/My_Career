class Solution:
    def removeElements(self, head , val):
        temp = head # текущий
        prev = None #предыдущий
        while temp != None:
            if head.val == val:#если значение головного узла равен val
                head = head.next#то головной узел перемещается
                temp = head#текщий будет головным узлом
                continue
            if temp.val == val:#если элемент текущего узла равен val
                temp = temp.next#то текущий узел перемещается
                prev.next = temp#предыдущий будет равен текущему
                continue
            temp = temp.next#текущий предвигается в следующий
            prev = temp#предыдущий равен текущему
        return head





        # while (head != None and head.val == val):
        #     head = head.next
        # prev = head
        # cur = head
        # while (cur != None):
        #     if (cur.val == val):
        #         cur = cur.next
        #         prev.next = cur
        #     else:
        #         prev = cur
        #         cur = cur.next
        #
        # return head