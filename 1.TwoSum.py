class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dict = {}
        for index , value in enumerate(nums):
            diff = target - value
            if diff not in dict :
                dict[value] = index
            else :
                return((dict[diff],index))

# sol = Solution()
# sol.twoSum([2, 7, 11, 15],9)

# nums = [2,11,7,15]
# target = 9
# dict = {}
# for index , value in enumerate(nums):
#     diff = target - value
#     if diff not in dict :
#         dict[value] = index
#     else :
#         print(dict[diff],index)