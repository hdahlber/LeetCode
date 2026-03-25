class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        for num in nums:
            if num in mydict:
                mydict[num] += 1
            else:
                mydict[num] = 1

        sorted_items = sorted(mydict.items(), key=lambda item: item[1], reverse=True)

        return [key for key, _ in sorted_items[:k]]

        