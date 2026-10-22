class Solution:
    def hammingWeight(self, n: int) -> int:
        #divison alg
        divisor = 1
        count = 0
        while n != 0:
            print(n)
            if n % 2 == 1:
                count += 1
            n  = math.floor(n/2)
        return (count)