class Solution:
    def isPalindrome(self, head):
        if not head:
            return True
        prev = None
        item = []
        temp = head
        while temp:#пока имеем текущий узел
            item.append(temp.val)#добавляем элмент текущего узла в массив
            next_ = temp.next#сохраняем следующий узел
            temp.next = prev #следующий равен предыдущему
            prev = temp #предыдущий равен текущему
            temp = next_#текущий равен следующему
        for i in item:
            if i != prev.val:
                return False
            prev = prev.next
        return True


        # vals = []
        # current_node = head
        # while current_node:
        #     vals.append(current_node.val)
        #     current_node = current_node.next
        # return bool(vals == vals[::-1])