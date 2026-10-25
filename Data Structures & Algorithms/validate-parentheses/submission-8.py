class Solution:
    def isValid(self, s: str) -> bool:
        #idea as we go along stack
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            else:
                if len(stack) == 0 or char != stack[-1]:
                    return False
                else:
                    stack.pop()
        if len(stack) != 0:
            return False
        return True

        