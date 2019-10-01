#初版
class Solution(object):        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def productTwoList(list1,list2):
            return [char1+char2 for char1 in list1 for char2 in list2]
            
        def getLetterCombinations(pre_list,index_count):
            if index_count>max_index:
                return pre_list
            else:
                digit = digits[index_count]
            
                if digit not in digits_mapping.keys():
                    return []
            
                pre_list = productTwoList(pre_list,digits_mapping[digit])
                result = getLetterCombinations(pre_list,index_count+1)
                return result
            
        digits_mapping={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        
        max_index = len(digits)-1
        
        if digits == "":
            return []
        
        ans =[""]
        ans = getLetterCombinations(ans,0)
        # print(ans)
        return ans