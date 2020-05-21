class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        intervals.sort()
        result = []
        low = intervals[0][0]
        high = intervals[0][1]
        for ele in intervals:
            if ele[0] <= high:
                if ele[1] >= high:
                    high = ele[1]
            else:
                result.append([low, high])
                low = ele[0]
                high = ele[1]
        result.append([low, high])

        return result
