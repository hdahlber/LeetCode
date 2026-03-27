class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            for word in strs:
                if word[i] != strs[0][i]:
                    result += strs[0][:i]
                    return result

        