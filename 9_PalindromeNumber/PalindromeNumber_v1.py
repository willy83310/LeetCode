import math
class Solution(object):
    def judgePalindrome(self, x , max_digit):
        quot,mod = divmod(x,10)
        
        if quot ==0 :
            return mod
        
        result = self.judgePalindrome(quot,max_digit-1)+mod*10**max_digit
        return result
        
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        max_digit = int(math.log10(x+0.1**10))+1
        # print(max_digit)
        reverse_int = self.judgePalindrome(x,max_digit-1)
        # print(reverse_int)
        if reverse_int == x:
            return True
        else:
            return False