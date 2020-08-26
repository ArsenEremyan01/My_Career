def xax(nums):
    dec = 0
    temp = 0
    for i in nums:
        if i == 1:
            temp = temp + 1
        if i == 0:
            dec = max(temp, dec) #переменная будет равна максимальному значению
            temp = 0
        if temp > dec:
            dec = temp
    return dec
a = [1,1,0,1,1,1]
print(xax(a))

#можно сократить код на пару строк в return поставив условие