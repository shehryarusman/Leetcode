#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        opp = {"{" : "}",
               "[": "]",
               "(":  ")"}
        hashMap = {}
        leftIdx = 0
        rightIdx = len(s)-1
        while leftIdx <= rightIdx:
            if s[leftIdx] in hashMap:
                hashMap[s[leftIdx]] +=1
            else:
                hashMap[s[leftIdx]] = 1
            if opp[s[leftIdx]] == s[rightIdx]:
                hashMap[s[leftIdx]] -=1
            else:
                return False
            leftIdx+=1
            rightIdx-=1
        for idx in range(len(s)):
            if s[idx] not in hashMap:
                continue
            if hashMap[s[idx]] == 0:
                continue
            else:
                return False
        return True
        
            
        
# @lc code=end

