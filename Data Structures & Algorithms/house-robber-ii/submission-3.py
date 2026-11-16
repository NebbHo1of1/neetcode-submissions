class Solution:
    def rob(self, nums: List[int]) -> int:
      if len(nums) <= 2:
        return max(nums)

      i = nums[0]
      j = max(nums[0], nums[1])

      for k in range(2, len(nums)-1):
        i, j = j, max(j, i + nums[k])

      l = nums[1]
      m = max(nums[1],nums[2])

      for n in range(3, len(nums)):
        l, m = m, max(m, l + nums[n])

      return max(j,m)

