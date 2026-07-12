class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float('-inf')

        def maxsum(node):
            nonlocal maxi

            if node is None:
                return 0

            leftsum = max(0, maxsum(node.left))
            rightsum = max(0, maxsum(node.right))

            maxi = max(maxi, leftsum + rightsum + node.val)

            return max(leftsum, rightsum) + node.val

        maxsum(root)
        return maxi