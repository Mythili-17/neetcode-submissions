from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        count = Counter(nums)
        res = []

        # Find duplicate
        for num in count:
            if count[num] == 2:
                res.append(num)
                break

        # Find missing
        for i in range(1, len(nums) + 1):
            if i not in count:
                res.append(i)
                break

        return res