#v2
class Solution(object):        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """ 
        def getLetterCombinations(combination,next_digits):
            if not next_digits:
                self.ans.append(combination)
                return
            else:
                next_digit = next_digits[0]
                if next_digit not in digits_mapping.keys():
                    self.ans = []
                    return
                
                for char in digits_mapping[next_digit]:
                    getLetterCombinations(combination+char,next_digits[1:])
            
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
        
        self.ans = []
        if digits:
            getLetterCombinations("",digits)
        # print(ans)
        return self.ans