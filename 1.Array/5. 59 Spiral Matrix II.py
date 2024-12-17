class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output = [[0] * n for _ in range(0, n)]
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        value = 1
        while left <= right:
            ## fill every val in the top row
            for c in range(top, right + 1):
                output[top][c] = value
                value += 1
            top += 1
            ## fill every val in the rightmost col
            for r in range(top, bottom + 1):
                output[r][right] = value
                value += 1
            right -= 1
            ## fill every val in the bottom row
            for c in range(right, left - 1, -1):
                output[bottom][c] = value
                value += 1
            bottom -= 1
            ## fill every val in the leftmost col
            for r in range(bottom, top - 1, -1):
                output[r][left] = value
                value += 1
            left += 1
        return output
