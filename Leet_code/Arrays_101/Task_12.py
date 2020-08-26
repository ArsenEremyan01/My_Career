def maxi(nums):
    nums = list(set(nums))#создаем множество тем самым удаляем дубликаты
    nums.sort()
    if len(nums) <= 2:
        return nums[-1]
    else:
        return nums[-3]



a = [3 , 2 , 1 , 5 , 7,8,9]
print(maxi(a))