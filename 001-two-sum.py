def twoSum(nums, target):
    hashmap = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], index]
        hashmap[num] = index
