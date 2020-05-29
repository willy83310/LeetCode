# Memory Limit Exceeded !!!!
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = nums[0]
        count = 0
        for num in nums:
            count += num
            if count < num:
                count = num
            if max_count < count:
                max_count = count

        return max_count
