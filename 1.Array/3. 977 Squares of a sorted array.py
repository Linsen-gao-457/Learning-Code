class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums2 = list()
        squared = list()
        for num in nums:
            nums2.append(num * num)
        L, R = 0, len(nums) - 1
        K = len(nums2)
        while K != 0:
            if nums2[L] < nums2[R]:
                squared.append(nums2[R])
                R -= 1
            else:
                squared.append(nums2[L])
                L += 1
            K -= 1
        squared.reverse()
        return squared
