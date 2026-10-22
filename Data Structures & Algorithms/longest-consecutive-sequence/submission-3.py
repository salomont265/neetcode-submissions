class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq ={}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        print(freq)
        if  not nums:
            return 0
       
        else:
            seq_max = 1
        for index,num in enumerate(nums):
            #start count
            if num - 1 not in freq:
                i = 1
                new_max = 1
                while num + i in freq:
                    new_max += 1
                    i += 1
                seq_max = max(new_max,seq_max)
        return seq_max
                