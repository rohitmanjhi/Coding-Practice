
class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def LCA(self, root, p, q):
        
        while root:
            # both left make
            if p.value < root.value and q.value < root.value:
                root = root.left

            # both right make
            if p.value > root.value and q.value > root.value:
                root = root.right

            # split hua ya root khud p/q hai
            else:
                return root     

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

p = root.left
q = root.right

solution = Solution()

ans = solution.LCA(root, p, q)

print(ans.value)
