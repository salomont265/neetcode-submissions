class Solution:
    def isValid(self, s: str) -> bool:
        #idea as we go along 
        to_close = []
        for char in s:
            print(char)
            #check if open breacket
            if char == '[':
                print('hh')
                to_close.insert(0,']')
            elif char == '(':
                to_close.insert(0,')')
            elif char == '{':
                to_close.insert(0,'}')
            #if is right
            else:
                if len(to_close) == 0 or char != to_close[0]:
                    return False
                to_close.pop(0)
        if len(to_close) != 0:
            return False
        return True