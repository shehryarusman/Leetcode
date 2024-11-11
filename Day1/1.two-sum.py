#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Naive Solution
        # Time Complexity - O(n^2)
        # Space Complexity - O(1)
        # for firstNum in range(len(nums)):
        #     for secondNum in range(len(nums)):
        #         if firstNum != secondNum and nums[firstNum]+nums[secondNum]==target:
        #             return firstNum, secondNum
        
        # Optimized Solution
        # Time Complexity - O(n)
        # Space Complexity - O(n)
        
        hashMap = {}
        for idx, num in enumerate(nums):
            hashMap[num] = idx 
            
        for idx in range(len(nums)):
            res = target-nums[idx]
            if res in hashMap and hashMap[res] != idx:
                return hashMap[res], idx 
       
        
# @lc code=end

