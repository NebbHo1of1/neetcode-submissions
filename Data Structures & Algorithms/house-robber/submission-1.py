class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return sum(nums)
        
        i = nums[0]
        j = max(nums[0],nums[1])

        for k in range(2, len(nums)):
            i, j = j, max(i + nums[k], j)
        
        return j
        