class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        fast = head.next
        slow = head
        while True:
            if fast is None or fast.next is None:#Если не имеем fast и fast.next то false
                return False
            elif fast.val == slow.val:#если значения указателей равны значит есть цикл
                return True
            else:
                slow = slow.next#иначе медленный указатель переводим дальше на один узел
                fast = fast.next.next#а быстрый указатель переводим дальше на два узла









