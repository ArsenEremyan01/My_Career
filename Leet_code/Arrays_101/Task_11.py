def stud(h):
    ls = []
    ls[:] = h #все элементы копируются
    h.sort()
    c = 0
    for i in range(len(h)):
        if ls[i] != h[i]:
            c += 1
    return c
    # result, new_h = 0, sorted(h)#new_h = h отсортированный
    # for i in range(len(h)):
    #     if new_h[i] != h[i]:
    #         result += 1
    # return result

s = [1,1,4,2,1,3]
print(stud(s))