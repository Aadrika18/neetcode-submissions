class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(start, target, path):
            if target == 0:
                ans.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])          # choose nums[i]
                dfs(i, target - nums[i], path)  # remaining = target - nums[i]
                path.pop()                    # backtrack

        dfs(0, target, [])
        return ans