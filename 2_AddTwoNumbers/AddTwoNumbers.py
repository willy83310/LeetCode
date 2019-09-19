# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_tmp = 0 
        result = ListNode(0)
        result_tail = result
        while l1 or l2 or carry_tmp :
            if l1==None :
                l1_val = 0
            else :
                l1_val = l1.val
            if l2==None :
                l2_val = 0
            else :
                l2_val = l2.val
            sum = l1_val + l2_val + carry_tmp
            result_tail.next = ListNode(sum%10)
            result_tail = result_tail.next
            
            if sum >= 10:
                carry_tmp = 1
            else :
                carry_tmp = 0
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next
