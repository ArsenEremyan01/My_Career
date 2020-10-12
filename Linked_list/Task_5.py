class Solution:
    def removeNthFromEnd(self, head,n):
        if head is None:
            return 0

        length = 0
        first = second = head #f и s в головном узле

        while first:#пока имеем f:
            first = first.next#передвигаем первый указатель на один узел
            length += 1#увеличиваем длину
            if length - 1 > n:# если длина-1 больше чем n то second переходит дальше
                second = second.next

        if length == n:
            return head.next

        else:
            second.next = second.next.next
            return head









# if head is None:
#     return 0
#
# first = second = head
#
# for i in range(n):
#     second = second.next
#
# if second is None:
#     return head.next
#
# while second.next is not None:
#     second = second.next
#     first = first.next
#
# first.next = first.next.next
#
# return head
