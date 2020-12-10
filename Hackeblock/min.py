# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    val: int
    left = None
    right = None

    def __int__(self, val):
        self.val: int = val
        self.left = None
        self.right = None


def minDepth(root: TreeNode) -> int:
    if root is None:
        return 0
    if root.left is None:
        return 1 + minDepth(root.right)
    if root.right is None:
        return 1 + minDepth(root.left)

    return 1 + min(minDepth(root.left), minDepth(root.right))


t = TreeNode()
t.val = 3
t.left = TreeNode()
t.left.val = 9
t.right = TreeNode()
t.right.val = 20
t.right.left = TreeNode()
t.right.left.val = 15
t.right.right = TreeNode()
t.right.right.val = 7
print(minDepth(t))
