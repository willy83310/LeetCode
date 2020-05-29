class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        low = newInterval[0]
        high = newInterval[1]
        if intervals == []:
            intervals.append(newInterval)
            return intervals
        if high < intervals[0][0] or low > intervals[-1][1]:
            intervals.append(newInterval)
            intervals.sort()
            return intervals
        # print(low,high)
        for interval in intervals:
            # print(interval)
            if high < interval[0] or low > interval[1]:
                result.append(interval)
            elif low <= interval[0] and high <= interval[1]:
                high = interval[1]
            elif low < interval[0] and high > interval[1]:
                continue
            elif low >= interval[0] and high <= interval[1]:
                low = interval[0]
                high = interval[1]
            else:
                low = interval[0]

            # print(low,high)
        result.append([low, high])
        result.sort()
        return result
