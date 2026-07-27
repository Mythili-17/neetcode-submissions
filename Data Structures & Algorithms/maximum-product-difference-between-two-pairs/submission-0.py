class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        nums.sort()

        n = len(nums)

        smallest1 = nums[0]
        smallest2 = nums[1]

        largest1 = nums[n - 1]
        largest2 = nums[n - 2]

        return (largest1 * largest2) - (smallest1 * smallest2)