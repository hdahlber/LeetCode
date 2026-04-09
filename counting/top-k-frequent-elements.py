from heapq import nlargest
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diction = {}
        for num in nums:
            try:
                value = diction[num]
                diction[num] = value + 1
            except:
                diction[num] = 1
        
        return nlargest(k, diction, key=diction.get)


        