
class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head.next
        while fast is not slow:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        while head is not slow:
            slow = slow.next
            head = head.next
        return head




        # try:
        #     slow = head
        #     fast = head.next
        #     while fast is not slow:
        #         slow = slow.next
        #         fast = fast.next.next
        # except:
        #     return None
        # slow = slow.next
        # while head is not slow:
        #     slow = slow.next
        #     head = head.next
        # return head
