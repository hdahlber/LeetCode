class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sum = 0
        start = False 
        for c in reversed(s):
            if not c.isspace():
                sum += 1
                if start == False:
                    start = True
            elif start == True:
                return sum
            else:
                continue
        return sum
        