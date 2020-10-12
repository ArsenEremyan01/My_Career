class Solution:
    def getIntersectionNode(self, headA, headB):

        first, second = headA, headB

        while first and second:
            if first == second:
                return first

            first = first.next
            second = second.next

            if first is None:
                first = headB
            if second is None:
                second = headA