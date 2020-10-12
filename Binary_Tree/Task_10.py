class Solution:
    def connect(self, root):
        if root is None:
            return root
        first = root#первый уровень равен корню
        while first.left:#пока имеем левое поддерево
            cur = first#текущий узел будет равен первому уровню т е корню до тех пор пока значение не поменяется
            while cur and cur.left:#пока имеем текущий и левое поддерево текущего
                cur.left.next = cur.right#следующий левого поддерева будет равен соседнему поддерево по уровню
                if cur.next and cur.right:
                    cur.right.next = cur.next.left#следующая вершина после правого поддерева
                                                  # будет равен левому поддерево левого поддерева
                cur = cur.next#текущий перейдет на соседний узел
            first = first.left#следующий уровень опускается в левое поддерево
        return root
