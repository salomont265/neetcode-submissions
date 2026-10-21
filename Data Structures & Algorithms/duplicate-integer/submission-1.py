class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic:dict = {}
        for index,num  in enumerate(nums):
            if num in dic:
                return True
            dic[num] = index
        return False
        