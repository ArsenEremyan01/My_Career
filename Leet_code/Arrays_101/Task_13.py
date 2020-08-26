def sort(nums):
    nums_input = set(nums)
    nums_output = set([i for i in range(1,len(nums)+1)])#генерируем числа которых не хватает в массиве
                                                        # исходя из колв-ва элементов в массиве

    return list(nums_output - nums_input)

a = [1,1,1]
print(sort(a))







