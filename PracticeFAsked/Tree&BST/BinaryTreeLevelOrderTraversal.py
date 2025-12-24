from collections import deque
class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if root is None: 
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result                


# root
root = TreeNode(6)

# level 1
root.left = TreeNode(2)
root.right = TreeNode(8)

# level 2
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)

root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# level 3
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

solution = Solution()

ans = solution.levelOrder(root)
print(ans)
