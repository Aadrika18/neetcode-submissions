# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.rightdfs(root, 0, res)
        return res

    def rightdfs(self, node, level, res):
        if node is None:
            return

        if level == len(res):
            res.append(node.val)

        self.rightdfs(node.right, level + 1, res)
        self.rightdfs(node.left, level + 1, res)