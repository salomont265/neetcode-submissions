class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,n in enumerate(nums):
            if target - n  in hashmap:
                return [hashmap[target-n],index]
            else:
                hashmap[n] = index

        