class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_value_mapping = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        result = 0
        pre_value = 0
        for char in s[::-1]:
            now_value = symbol_value_mapping[char]
            if now_value < pre_value :
                result-=now_value
            else:
                result+=now_value
            pre_value = now_value
            
        return result