from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = []
        count = Counter(arr)

        for num in arr:
            if count[num] == num:
                res.append(num)

        if not res:
            return -1

        return max(res)