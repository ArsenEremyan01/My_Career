class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if val > root.val:
                return self.searchBST(root.right, val)
            if val < root.val:
                return self.searchBST(root.left, val)
            else:
                return root
        else:
            return None