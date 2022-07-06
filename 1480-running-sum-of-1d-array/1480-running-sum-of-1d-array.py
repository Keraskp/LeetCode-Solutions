class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        add = nums[0]
        for i in range(1,len(nums)):
            nums[i] += add
            add = nums[i]
            
            
        return nums