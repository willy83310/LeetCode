# memory limit exceed


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        result = False
        for needed_step, max_step in enumerate(nums[-2::-1], 1):
            # print(needed_step,max_step)
            if len(nums)-1 <= nums[0]:
                return True
            if needed_step <= max_step:
                result = self.canJump(nums[:-needed_step])
                # print(result)
                return result
            else:
                return False

        return result
