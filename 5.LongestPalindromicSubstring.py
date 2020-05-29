class Solution(object):
    def judge_palindromic(self,index1,index2,max_index):
        string = self.string
        # print("method",index1,index2)
        # print(string[index1],string[index2])
        
        if index1==-1 or index2==max_index+1 or string[index1]!=string[index2]:
            return string[index1+1:index2]
            
        
        if string[index1]==string[index2]:
            result = self.judge_palindromic(index1-1,index2+1,max_index) 
        
            return result
        
    def get_duplica_number_index(self,index,max_index):
        string = self.string
        if index==max_index:
            return max_index 
        
        if string[index]==string[index+1]:
            result = self.get_duplica_number_index(index+1,max_index)
            return result
        else:
            return index
        
    def longestPalindrome(self, string):
        """
        :type s: str
        :rtype: str
        """
        self.string = string
        result = ""
        max_index = len(string)-1
        start_char = 0
        while start_char <= max_index:
            end_char = self.get_duplica_number_index(start_char , max_index)
            # print(start_char,end_char)
            result_tmp = self.judge_palindromic(start_char,end_char,max_index)
            if len(result_tmp) > len(result):
                result = result_tmp
            # result.append(self.judge_palindromic(start_char,end_char,max_index))
            # print(result)
            start_char = end_char+1
        return result