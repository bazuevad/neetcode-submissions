class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]

        for i in nums[:-1]:
            left.append(left[-1]*i)
        right = [1]
        for i in reversed(nums[1:]):
            right.append(right[-1]*i)
        right.reverse()

        answ = []
        for i in range(len(nums)):
            answ.append(left[i]*right[i])
        return answ