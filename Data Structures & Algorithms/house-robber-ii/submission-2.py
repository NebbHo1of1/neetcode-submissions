class Solution:
    def rob(self, nums: List[int]) -> int:
      if len(nums) <= 2:
        return max(nums)

      houses = nums[:-1]

      i = houses[0]
      j = max(houses[0], houses[1])

      for k in range(2, len(houses)):
        i, j = j, max(j, i + houses[k])

      houses2 = nums[1:]

      l = houses2[0]
      m = max(houses2[0],houses2[1])

      for n in range(2, len(houses2)):
        l, m = m, max(m, l + houses2[n])

      return max(j,m)
      
