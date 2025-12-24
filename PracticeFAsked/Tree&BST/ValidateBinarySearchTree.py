class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        self.prev = None

        def inOrder(node):
            if node:
                print(node.val)
            if node is None:
                return True

            if not inOrder(node.left):
                return False

            if self.prev is not None and node.val <= self.prev:
                return False

            self.prev = node.val

            return inOrder(node.right)

        return inOrder(root)                 

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

solution = Solution()

ans = solution.isValidBST(root)

print(ans)
