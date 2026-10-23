class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        for index,num in enumerate(nums):
        #check if positive, fi so its over
            if num>0:
                break
            if index> 0 and nums[index] == nums[index-1]:
                continue
        #setup for loop
            l,r = index + 1,len(nums)-1

            while l<r:
               
            #conditons time baby
                if num + nums[l] + nums[r] ==0:
                    #found an answer
                    res.append([num,nums[l],nums[r]])
                    #shiftl and r
                    l += 1
                    r -= 1
              
                    #check duplciate
                   
                    while l<r and nums[l] == nums[l-1]:
                        
                        l += 1
                #other option, l is too smal
                elif num + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return res

