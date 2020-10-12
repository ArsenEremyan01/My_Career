class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        cur = head# текущий
        length = 0
        while cur:# пока имеем текущий узел
            length += 1# увеличиваем длину
            cur = cur.next# проверяем следующий узел
# первая часть находим длину списка
        dummy = ListNode()# создаем фиктивный узел перед head
        dummy.next = head
        slow, fast = dummy, dummy.next# медленный указатель находится перед головным , а быстрый на головном узле

        k = k % length# проверяем k
        if k == 0:
            return head
        else:
            for _ in range(k):#проходим цикл на к шагов
                fast = fast.next#fast передвигаем на k шагов
            slow = slow.next#slow на один шаг

            while fast.next:#пока имеем fast.next, переводим указатели дальше
                fast = fast.next
                slow = slow.next

            newHead = slow.next#slow.next будет равен головному узлу
            fast.next = dummy.next#узел fast.next будет после
            slow.next = None#
            return newHead#

















        # if head == None or k == 0:
        #     return head
        # temp = head
        # length = 0
        # while temp:
        #     temp = temp.next
        # length = length + 1
        #
        # for _ in range(k % length):
        #     temp = head
        #     dummy = temp
        #     while temp.next:
        #         dummy = temp
        #         temp = temp.next
        #     temp.next = head
        #     head = temp
        #     dummy.next = None
        # return head