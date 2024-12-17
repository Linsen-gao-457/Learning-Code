class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        while right >= left:
            middle = (right + left) // 2
            if target > nums[middle]:
                middle = left + 1
            elif target < nums[middle]:
                middle = right - 1
            else:
                return middle
        return -1


nums = [1, 3, 5, 7, 9]
target = 5
solution = Solution()
index = solution.search(nums, target)
print(index)
