## Memory Limit Exceeded !!!!
class Solution(object):  
    def findMaxSubArray(self,tmp,ans,next_nums):
        if tmp >= ans:
            ans = tmp
        if len(next_nums)==0:
            return ans
        if tmp >= 0:
            if next_nums[0]>=0:
                tmp+=next_nums[0]
                result = self.findMaxSubArray(tmp,ans,next_nums[1:])
            else:
                if tmp+next_nums[0]>=0:
                    tmp+=next_nums[0]
                else:
                    tmp = 0
                result = self.findMaxSubArray(tmp,ans,next_nums[1:])
            return result
        else:
            tmp = next_nums[0]
            result = self.findMaxSubArray(tmp,ans,next_nums[1:])
            return result
        
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = nums[0]
        ans = nums[0]
        if nums[1:]:
            ans = self.findMaxSubArray(tmp,ans,nums[1:])
        return(ans)