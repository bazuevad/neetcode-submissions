class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def backtrack(curr):
            if curr==n:
                return 1
            if curr>n:
                return 0
            if curr in memo:
                return memo[curr]
            memo[curr] = backtrack(curr+1)+backtrack(curr+2)
            return memo[curr]

        return backtrack(0)


            