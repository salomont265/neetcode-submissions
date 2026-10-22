class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers) -1

        while l < r:
            diff = target - numbers[r]
            if numbers[l] == diff:
                return [l+1,r+1]
            if diff > numbers[l]:
                l += 1
            else:
                r -= 1
        