class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def dfs(l, r):
            # Base case: no elements
            if l > r:
                return float("-inf")
            
            m = (l + r) >> 1
            
            leftSum = rightSum = currSum = 0
            
            # Find maximum subarray sum extending left from middle
            for i in range(m - 1, l - 1, -1):
                currSum += nums[i]
                leftSum = max(leftSum, currSum)

            # Find maximum subarray sum extending right from middle
            currSum = 0
            for i in range(m + 1, r + 1):
                currSum += nums[i]
                rightSum = max(rightSum, currSum)
            
            return max(
                dfs(l, m - 1),
                dfs(m + 1, r),
                leftSum + nums[m] + rightSum
            )

        return dfs(0, len(nums) - 1)