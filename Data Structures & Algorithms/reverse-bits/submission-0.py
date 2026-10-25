class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            l = n & 1
            print(l)
            n >>= 1
            res = res << 1 | l
        return res
        