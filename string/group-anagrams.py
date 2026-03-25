class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for string in strs:
            key = "".join(sorted(string))
            if key not in mydict:
                mydict[key] = []
            mydict[key].append(string)
        return list(mydict.values())