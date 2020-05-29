class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        start_index=0
        end_index = len(height)-1
        while start_index != end_index:
            area_tmp = (end_index-start_index)*min(height[start_index],height[end_index])
            if area_tmp > area:
                area = area_tmp
            if height[end_index] >= height[start_index]:
                start_index+=1
            else:
                end_index-=1
                
                
        return area