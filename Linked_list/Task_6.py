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

#recursive
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        if head.next is None:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res
        # def reverse_helper(node, prev = None):
        #     if not node:
        #         return prev
        #     after = node.next
        #     node.next = prev
        #     return reverse_helper(after,node)
        # return reverse_helper(head)
