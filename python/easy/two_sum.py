import sys
from typing import List

#given an array and a target, return the values of the indexes that add up to the target

class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+ nums[j]==target):
                    return [nums[i],nums[j]]
        return []

if __name__ == '__main__':
    solution = Solution()
    test_case_array=[2,7,11,15]
    print(solution.twoSum(test_case_array,21))
    


