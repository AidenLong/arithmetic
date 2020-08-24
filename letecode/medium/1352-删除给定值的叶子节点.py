# -*- coding utf-8 -*- #

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root


if __name__ == '__main__':
    root = TreeNode(1)
    left1 = TreeNode(2)
    right1 = TreeNode(3)
    left2_1 = TreeNode(2)
    left2_2 = TreeNode(2)
    right2_2 = TreeNode(4)
    root.left = left1
    root.right = right1
    left1.left = left2_1
    right1.left = left2_2
    right1.right = right2_2
    s = Solution()
    result = s.removeLeafNodes(root, 2)
    print(result)
