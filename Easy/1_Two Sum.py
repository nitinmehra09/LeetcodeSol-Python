class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for ind1 in range (len(nums)):
            for ind2 in range(ind1+1,len(nums)):
                if (nums[ind1]+nums[ind2]==target):
                    return [ind1,ind2]
                