class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        freq = [ [] for i in range(len(nums)+1)]

        for index,num in enumerate(nums):
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        for key,value in dict.items():
            freq[value].append(key)
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
