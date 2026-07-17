class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(curr,i,total):
            if total==target:
                res.append(curr[:])
                return
            if i>=len(nums) or total > target:
                return
            curr.append(nums[i])
            backtrack(curr,i,total+nums[i])
            curr.pop()
            backtrack(curr,i+1,total)

        backtrack([],0,0)
        return res