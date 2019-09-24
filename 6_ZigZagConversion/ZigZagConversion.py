class Solution(object):
        
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1 or numRows == 0:
            return s
        
        result = [""]*numRows
        
        for index in range(len(s)):
            index_tmp = index%(numRows*2-2)
            group = (numRows*2-2-index_tmp) if index_tmp > (numRows-1) else index_tmp
            # print(group)
            result[group]+=s[index]
        
        ans = "".join(result)
        # print(ans)
        
        return ans