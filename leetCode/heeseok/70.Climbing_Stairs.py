class Solution:
    def climbStairs(self, n: int) -> int:
        stepsList = [1, 2]
        if n < 2:
            return 1
        elif n == 2:
            return 2
        for i in range(2, n):
            stepsList.append(stepsList[i - 1] + stepsList[i - 2])
        return stepsList[-1]


result = Solution().climbStairs(5)
print(result)
