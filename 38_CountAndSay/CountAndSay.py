import itertools
class Solution(object):
    def find_seq_str(self,seq,n):
        if n==1:
            return seq
        else:
            next_str =""
            for ele,iter_item in itertools.groupby(seq):
                # print(ele,list(iter_item))
                count = len(list(iter_item)) 
                next_str += (str(count)+ele) 
            result = self.find_seq_str(next_str,n-1)
            return result
                
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = self.find_seq_str("1",n)
        return result