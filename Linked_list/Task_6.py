class Solution:
    def reverseList(self, head):
        if head is None:
            return 0
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        head = prev
        return head

