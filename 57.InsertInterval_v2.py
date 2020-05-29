class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        low = newInterval[0]
        high = newInterval[1]
        left, right = [], []
        for interval in intervals:
            if high < interval[0]:
                right.append(interval)
            elif low > interval[1]:
                left.append(interval)
            else:
                low = min(low, interval[0])
                high = max(high, interval[1])
        return left+[[low, high]]+right
