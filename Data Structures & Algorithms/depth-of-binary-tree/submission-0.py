class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def dfs(node):
            if node is None:
                return 0
            else:
                left_h = dfs(node.left)
                right_h = dfs(node.right)
                return max(left_h, right_h) + 1
        
        return dfs(root)