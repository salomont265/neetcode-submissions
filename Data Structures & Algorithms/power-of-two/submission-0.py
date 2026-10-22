class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        n2 = n
        if n == 1:
            return True
        count = 0
       
        while n2 >= 2:
            n2= n2 // 2
            print(n2)
            count += 1
        print(count)
        if n - 2**count ==  0:
            return True
        return False
       