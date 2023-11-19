class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            value = nums[i]
            complementValue = target - value
            if complementValue in map:
                return [ map[complementValue], i ]
            else:
                map[value] = i
input_list = [2,8,12,15]
ob1 = Solution()
print(ob1.twoSum(input_list, 20))