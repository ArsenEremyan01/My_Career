class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)#задаем значение первое val
        cur = res
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1 == None and l2 == None:
            return res.next

        while l1 and l2:
            if l1.val > l2.val:#если элемент n-ого узла первого списка больше чем у второго
                cur.next = l2#текущий узел сохранит узел второго списка
                l2 = l2.next#узел второго списка перейдет на следующий узел

            else:
                cur.next = l1#иначе текущий сохранит узел первого списка
                l1 = l1.next
            cur = cur.next#текущий элемент передвигается на следующий

        cur.next = l1 or l2#

        return res.next