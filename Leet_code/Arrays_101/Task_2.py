def find_number(a):
    result = 0
    for i in range(len(a)):
        if len(str(a[i])) % 2 == 0:#находим длину строки то есть числа и проверяем на четность
            result = result + 1
    return result
x = [12,345,2,6,7896]
print(find_number(x))
