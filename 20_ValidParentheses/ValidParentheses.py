class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_mapping = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        tmp_list=[]
        if s=="":
            return True
        for char in s:
            if char in char_mapping.keys():
                tmp_list.append(char)
            elif tmp_list==[] and char in char_mapping.values():
                return False
            elif char_mapping[tmp_list[-1]] != char:
                return False
            else :
                tmp_list.pop()
        if tmp_list!=[]:
            return False
        else:
            return True