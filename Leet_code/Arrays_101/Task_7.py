def bin(arr):
    if arr.count(0) > 1: #если кол-во нулей больше 1 то True
        return True
    for i in arr:
        if i != 0 and i * 2 in arr: #если i не равно 0 и если существует такое что = i * 2 то True
            return True
    return False


a = [-2,0,10,-19,4,6,-8]
print(bin(a))


