def kvad(x):
    # return sorted([i**2 for i in x])
    c = []
    for i in x:
        c.append((i ** 2))
        c.sort()
    return c

a = [-4,-1,0,3,10]
print(kvad(a))


