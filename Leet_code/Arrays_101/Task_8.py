def zam(arr):
    c = -1
    for i in range(len(arr)-1,-1,-1):
        s = arr[i]
        arr[i] = c #последний элемент будет равен -1
        c = max(c,s) #далее c будет равно максимульному числу из c и s
    return arr

a = [17,18,5,4,6,1]
print(zam(a))
#
# def zam(arr):
#     for i in range(len(arr) - 1):
#         arr[i] = max(arr[i + 1:])#число i будет равен максимальному число справа от i последнего
#     arr[-1] = -1
#     return arr

# a = [17,18,5,4,6,1]
# print(zam(a))

