class Solution:
    def twoSum(nums, target) -> int:
        sums = {}
        for i in range(len(nums)):
            number = nums[i]
            complement = target - number
            if complement in sums:
                return [sums[complement], i]
            else:
                sums[number] = i
        return -1
