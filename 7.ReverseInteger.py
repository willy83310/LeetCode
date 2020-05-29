## 遞迴
import math
class Solution(object):
    def get_reverse(self,x,dig):
        
        quot , mod = divmod(x,10)
        
        if quot == 0 :
            return mod
        
        result = self.get_reverse(quot,dig-1) + mod*10**dig
        return result
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2**31-1 or x < -2**31 or x==0:
            return 0
        
        if x < 0:
            x = abs(x)
            result = -1
        else:
            result = 1
        
        dig = int(math.log10(x))+1
        # print("info :",dig)
        
        result = result * self.get_reverse(x,dig-1)
        
        if result > 2**31-1 or result < -2**31:
            return 0
        
        return result