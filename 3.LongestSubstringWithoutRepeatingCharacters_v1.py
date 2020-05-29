## 暴力解 (字串太大會time exceed)
class Solution(object):
    def check_str_repeat(self,test_string):
        if len(test_string) == len(set(test_string)):
            return 1
        else:
            return 0
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = ""
        for start_char in range(len(s)):
            for end_char in range(start_char,len(s)+1):
                test_string = s[start_char:end_char]
                # print(test_string)
                if self.check_str_repeat(test_string)==0:
                    break
                else:
                    if len(test_string)>len(result):
                        result=test_string
        print(result)
        return(len(result))