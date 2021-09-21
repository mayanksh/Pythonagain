nums = [0,1,2,3,4]
index = [0,1,2,2,1]
target = []
for i in range(len(nums)):
    target.insert(index[i], nums[i]) #nums(x,i) x signify the index in the list, which you are going to insert i

print(target)
