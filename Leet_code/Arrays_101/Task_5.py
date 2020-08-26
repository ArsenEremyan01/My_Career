def rem(nums,val):
    a = nums[:]
    for i in a:# запуск цикла по всем элементам
        if i == val:
            nums.remove(i)
    return len(nums)
vall = 3
numss = [3,2,2,3]
print(rem(numss,vall))


#a = [i for i in nums[:] if i != val ]