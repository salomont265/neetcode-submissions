class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        total = 0
        for n in nums:
            total += n
            mx = max(mx,total)
            if total < 0:
                total = 0
        return mx

        