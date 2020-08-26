def rem_dup(x):
    if len(x) == 0:
        return 0
    a = 0
    for i in range(len(x)):
        if x[i] == x[a]:#если i-ый элемент равен элементу а то ничего не делается
            pass
        else:
            a += 1#счетчик
            x[a] = x[i]#элемент а перемещается на место i-того элемента
    return a + 1 #так как при замене элементов появляется еще один дубликат прибавляем единицу к счетчику

nums = [0,0,1,1,1,2,2,3,3,4]
print(rem_dup(nums))

# x[:] = list(set(x))
# return len(sorted(x))


