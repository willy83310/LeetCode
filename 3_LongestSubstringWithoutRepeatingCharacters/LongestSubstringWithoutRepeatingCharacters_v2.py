# v2
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
        start_char = 0
        position_dic = {}
        dic = {}
        for end_char in range(len(s)):
            test_string=s[start_char:end_char+1]
            if s[end_char] not in position_dic.keys():
                position_dic[s[end_char]] = end_char
            else :
                if position_dic[test_string[-1]] >= start_char:
                    start_char = position_dic[test_string[-1]]+1
#               position_dic = {}
                position_dic[s[end_char]] = end_char
#               print("abc",s[start_char:end_char+1])
                if self.check_str_repeat(s[start_char:end_char+1]) ==1 :
                    if len(s[start_char:end_char+1]) not in dic.keys():
                        dic[len(s[start_char:end_char+1])]=[]
                    dic[len(s[start_char:end_char+1])].append(s[start_char:end_char+1])
        
        
            if self.check_str_repeat(test_string)==1:
                if len(test_string) not in dic.keys():
                    dic[len(test_string)]=[]
                dic[len(test_string)].append(test_string)
                
        if dic == {}:
            return 0
        else:
            return max(dic.keys())