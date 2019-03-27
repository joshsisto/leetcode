#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
### Example
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
###

nums = [2, 7, 11, 15]
target = 9


"""
def twoSum(nums, target):
    hashMap = {}
    for i in range(len(nums)):
        print(f'============{hashMap}=============')
        print(f'This is i {i}')
        x = nums[i]
        print(f'This is x {x}')
        if x in hashMap:
            # return [hashMap[x], i]
            print([hashMap[x], i])
        else:
            hashMap[target - x] = i
"""


def twoSum(nums, target):
    if len(nums) < 2:
        pass
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sums = nums[i] + nums[j]
            if sums == target:
                print([i, j])
                return [i, j]


twoSum(nums, target)
