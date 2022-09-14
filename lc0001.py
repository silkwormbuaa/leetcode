# -*- coding: utf-8 -*-
'''
@File    :   lc0001.py
@Time    :   2022/08/24 16:37:19
@Author  :   Wencan WU 
@Version :   1.0
@Email   :   w.wu-3@tudelft.nl
@Desc    :   None
'''
from typing import List, Optional
#%% my answer
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsLen = len(nums)
        Inx = []
        for i in range(numsLen):
            for j in range(1,(numsLen-i)):
                Sum = nums[i] + nums[i+j]
                if Sum == target :
                    Inx.append(i)
                    Inx.append(i+j)
                    break
        print(Inx)

#%% Best solution
class Solutions:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                print(hashtable[target - num],i)
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

        
S = Solutions()
S.twoSum([4,3,2,11,7,15],9)

mine = Solution()
mine.twoSum([4,3,2,11,7,15],9)