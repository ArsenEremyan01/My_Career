class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = ''
        b = ''
        l3 = ListNode()#создаем новый лист
        temp = l3
        while l1:
            cur = str(l1.val)
            a = cur + a#добавляем элементы в строку а
            l1 = l1.next#перемещаемся дальше
        while l2:
            cur = str(l2.val)
            b = cur + b
            l2 = l2.next
        res = int(a) + int(b)
        stop = 0
        for i in str(res)[::-1]:#начинаем цикл с конца
            temp.val = i#Текущий элемент равен i
            if stop == len(str(res))-1:
                break
            temp.next = ListNode()#последующий узел равен новому списку
            temp = temp.next#текущий равен следующему
            stop += 1
        return l3