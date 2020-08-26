def dup(arr):
    temp = 0
    while temp < len(arr) - 1:
        if arr[temp] == 0:
            arr.insert(temp + 1, 0)#вставляем ноль рядом с temp
            temp += 1 #каждой иттерацией число сдвигается правее
            arr.pop()#по умолчанию удаляем последний элемент чтобы не менялся размер массива
        temp += 1#счетчик
    return arr

x = [1, 0, 2, 3, 0, 4, 5, 0]
print(dup(x))

