class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        sum = 0
        result = len(nums)
        Found = False
        while i <= len(nums) - 1:
            sum += nums[i]
            i += 1
            while sum >= target:
                sum -= nums[j]
                Found = True
                subLength = i - j
                result = min(result, subLength)
                if j != len(nums) - 1:
                    j += 1
        return result if Found else 0
