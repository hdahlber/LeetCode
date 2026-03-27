class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        while i < len(s) and i < len(t) and s[i] == t[i]:
            i += 1
        return len(t) - len(t[:i])
        
        