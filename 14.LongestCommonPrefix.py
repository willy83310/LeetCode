class Solution(object):
    def get_longest_prefix_string(self,old_string,new_string,index=0):
        # print(index)
        # print(old_string,new_string)
        if index==min(len(old_string),len(new_string)):
            return index
        if old_string[index]!=new_string[index]:
            return index
        if old_string[index]==new_string[index]:
            final_index = self.get_longest_prefix_string(old_string,new_string,index+1)
            return final_index
        
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ""
        old_string = strs[0]
        for index in range(len(strs)-1):
            if old_string=="" or strs[index+1]=="":
                return ""
            old_string = old_string[0:self.get_longest_prefix_string(old_string,strs[index+1])]
            
            
        return old_string