def twoSum(nums, target):
    tar_list = [target - i for i in nums]
    hash = {}
    for i in nums:
        hash[i] = 1

    index_1 = 0
    index_2 = 0
    value_2 = 0
    for i in range(len(tar_list)):
        if hash[tar_list[i]]==1:
            index_1 = i
            value_2 = tar_list[i]
            break
            
    for i in range(len(nums)):
        if nums[i] == value_2:
            index_2 = i
            
    return(sorted([index_1, index_2]))        

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))