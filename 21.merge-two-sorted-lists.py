# !!!!!!!!!!!! uncomplete

#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        count = 0
        result = ListNode()
        while count < 4:
            if l1.val > l2.val:
                tmp = ListNode(l2.val)
                result.next = tmp
                l2 = l2.next
            else:
                tmp = ListNode(l1.val)
                result.next = tmp
                l1 = l1.next

            # result = result.next
            count += 1
        print(result)
        return result
# @lc code=end
