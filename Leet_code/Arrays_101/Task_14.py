def mount(x):
    if len(x) < 3:
        return False
    maxi = x.index(max(x))#индекс максимального числа из массива x
    if maxi == len(x)-1 or maxi == 0:# проверяем на то где находится максимальный элемент
        return False
    for i in range(0,maxi):#проверка элементов до максимального элемента
        if x[i] > x[i+1]:
            return False
    for i in range(maxi,len(x)-1):#проверка элементов c максимального элемента и до конца
        if x[i] <= x[i+1]:
            return False
    return True
a = [0,3,2,1]
print(mount(a))



