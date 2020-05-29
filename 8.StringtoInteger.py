class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result_str = ""
        for char in str:
            if ord(char) in range(48,58) : 
                result_str+=char
            
            elif result_str=="" and (ord(char) == 45 or ord(char) == 43):
                result_str+=char
            
            elif result_str=="" and ord(char)==32:
                continue
            
            else:
                break
                
        # print result_str
        
        if result_str=="" or result_str=="-" or result_str=="+":
            return 0
        else:
            result = int(result_str)
            if result > 2**31-1:
                return 2**31-1
            elif result < -2**31:
                return -2**31
            else:
                return result