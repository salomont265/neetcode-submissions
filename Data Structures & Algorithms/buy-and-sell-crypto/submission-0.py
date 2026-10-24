class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0
        for num in prices:
            if num < min:
                min = num
            else:
                temp = num - min
                print(temp)
                print(profit)
                profit = max(profit,temp)
        return profit