#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Naive Solution
        # Time Complexity - O(m+n)
        # Space Complexity - O(m+n)
        
        head = ListNode()
        l = head
        carry = 0
        
        while l1!= None or l2!= None:
            ans = ListNode()
            if carry:
                value = l1.val+l2.val+1
            else:
                value = l1.val + l2.val
            if value > 9:
                value = value%10
                carry = 1
            else:
                carry = 0
            ans.val = value
            l1 = l1.next
            l2 = l2.next
            l.next = ans
            l = l.next
        while l2!= None:
            ans = ListNode()
            if carry:
                value = l2.val + 1
            else:
                value = l2.val
            if value > 9:
                value = value%10
                carry = 1
            else:
                carry = 0
            ans.val = value   
            l2 = l2.next
            l.next = ans
            l = l.next
        while l1!= None:
            ans = ListNode()
            ans.value = l1.val
            if carry:
                value = l1.val + 1
            else:
                value = l1.val
            if value > 9:
                value = value%10
                carry = 1
            else:
                carry = 0
            ans.val = value    
            l1 = l1.next
            l.next = ans
            l = l.next
        if carry:
            ans = ListNode()
            ans.val = 1
            l.next = ans

        return head.next
        
# @lc code=end

