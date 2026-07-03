class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo = i + 1
            hi = n - 1
            while lo<hi:
                summy = nums[i]+nums[lo]+nums[hi]
                if summy==0:
                    output.append((nums[i],nums[lo],nums[hi]))
                    lo+=1
                    hi-=1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1 
                elif summy<0:
                    lo+=1
                else:
                    hi-=1
        return output