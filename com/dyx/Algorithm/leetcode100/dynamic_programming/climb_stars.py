class Solution:
    def climbStairs(self, n: int) -> int:
        # 状态转移公式dp(i) = dp(i-1) + dp(i-2)
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = 0
        dp0 = 1
        dp1 = 2
        for i in range(2, n):
            dp = dp1 + dp0
            dp0 = dp1
            dp1 = dp
        return dp