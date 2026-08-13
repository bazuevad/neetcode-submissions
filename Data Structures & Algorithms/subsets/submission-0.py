class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = []
        def helper(start):
            if start>=len(nums):
                output.append(subset.copy())
                return
            subset.append(nums[start])
            helper(start+1)
            subset.pop()
            helper(start+1)
            return 
        helper(0)
        return output

