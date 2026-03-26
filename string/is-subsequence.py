class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pattern = ".*".join(s)
        return re.search(pattern, t) is not None