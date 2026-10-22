class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(char for char in s if char.isalnum()).lower()
        length = int(len(clean) /2)
        # print(length)
        for i in range(length):
            # print(i)
            if clean[i] != clean[len(clean)-1 - i]:
                return False

        return True