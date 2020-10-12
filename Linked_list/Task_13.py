class Solution:
    def copyRandomList(self, head):

        node = head
        while node:
            next = node.next
            copy = Node(node.val, node.next, node.random)
            node.next = copy
            node = next

        node = head

        while node:
            if node.random:
                node.next.random = node.random.next

            node = node.next.next

        dummy = Node(0)
        prev = dummy
        node = head
        while node:
            prev.next = node.next
            node.next = node.next.next
            node = node.next
            prev = prev.next

        return dummy.next
