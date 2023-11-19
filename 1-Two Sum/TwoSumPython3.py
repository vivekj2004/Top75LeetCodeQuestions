# from typing import *
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #### def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            value = nums[i]
            complement = target - value
            if complement in map:
                return [map[complement], i]
            else:
                map[value] = i

input_list = [2,8,12,15]
ob1 = Solution()
print(ob1.twoSum(input_list, 20))