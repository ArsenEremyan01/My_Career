def preorderTraversal(self, root):
    if not root:
        return []
    node, res = [], []
    while root or node: #пока имеем корень или узлы
        if root is not None: #если корневой узел существует
            node.append(root) #то корневой узел добавляем в node
            res.append(root.val) #а значение корневого узла в res
            root = root.left #корневой узел переходит на левый дочерний узел
        else: #если корневого узла нет
            root = node.pop() #то корневой узел будет равен последнему в node добавленному узлу
            root = root.right #и перейдет на правый дочерний узел
    return res


# if not root:
#     return []
# ret = [root.val]
# ret += self.preorderTraversal(root.left)
# ret += self.preorderTraversal(root.right)
# return ret